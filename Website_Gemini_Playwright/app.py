import asyncio
import os
import re
from urllib.parse import quote_plus

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")


def make_search_query(user_request: str) -> str:
    """Use Gemini to turn a natural-language shopping request into a concise search phrase."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        # Preserve the ability to use Playwright even when Gemini is not configured.
        return user_request.strip()

    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=(
                "Convert this shopping request into one concise Amazon India product "
                "search query. Keep important brand, product type, budget and features. "
                "Return only the search query, with no quotes or explanation.\n"
                f"Request: {user_request}"
            ),
        )
        query = (response.text or "").strip().strip('"').strip("'")
        return query or user_request.strip()
    except Exception as exc:
        # Do not expose API keys or full provider exceptions to the browser.
        raise RuntimeError(
            "Gemini could not process the request. Check GEMINI_API_KEY, model access, and internet connection."
        ) from None


async def amazon_search(search_query: str):
    """Open Amazon India with Playwright, search, and collect visible product cards."""
    from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            context = await browser.new_context(
                locale="en-IN",
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                ),
            )
            page = await context.new_page()
            await page.goto(
                "https://www.amazon.in",
                wait_until="domcontentloaded",
                timeout=60000,
            )

            search_box = page.locator("#twotabsearchtextbox")
            await search_box.wait_for(state="visible", timeout=20000)
            await search_box.fill(search_query)
            await page.locator("#nav-search-submit-button").click()

            try:
                await page.wait_for_selector(
                    "[data-component-type='s-search-result']",
                    timeout=25000,
                )
            except PlaywrightTimeoutError:
                title = await page.title()
                if "robot" in title.lower() or "captcha" in (await page.locator("body").inner_text()).lower():
                    raise RuntimeError(
                        "Amazon displayed a CAPTCHA or bot-check page. Try again later or use a normal browser session."
                    ) from None
                raise RuntimeError(
                    "Amazon search results did not load. Amazon may have changed its page or blocked automated access."
                ) from None

            cards = page.locator("[data-component-type='s-search-result']")
            count = min(await cards.count(), 12)
            products = []

            for i in range(count):
                card = cards.nth(i)
                try:
                    title_locator = card.locator("h2 a span").first
                    name = (await title_locator.inner_text(timeout=2500)).strip()
                    link = await card.locator("h2 a").first.get_attribute("href")
                    if link and link.startswith("/"):
                        link = "https://www.amazon.in" + link
                    elif link and not link.startswith("http"):
                        link = "https://www.amazon.in/" + link

                    price = ""
                    price_locator = card.locator(".a-price .a-offscreen").first
                    if await price_locator.count():
                        price = (await price_locator.inner_text(timeout=1500)).strip()

                    rating = ""
                    rating_locator = card.locator("span.a-icon-alt").first
                    if await rating_locator.count():
                        rating = (await rating_locator.inner_text(timeout=1500)).strip()

                    if name:
                        products.append({
                            "name": name,
                            "price": price or "Price not shown",
                            "rating": rating or "Rating not shown",
                            "url": link or "",
                        })
                except Exception:
                    # Skip cards with incomplete/unexpected markup.
                    continue

            return {
                "query": search_query,
                "title": await page.title(),
                "url": page.url,
                "products": products,
            }
        finally:
            await browser.close()


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/api/search")
def search():
    payload = request.get_json(silent=True) or {}
    user_request = payload.get("query", "")

    if not isinstance(user_request, str) or not user_request.strip():
        return jsonify(error="Enter a product or shopping request."), 400
    if len(user_request) > 500:
        return jsonify(error="Search request is too long (maximum 500 characters)."), 400

    try:
        search_query = make_search_query(user_request.strip())
        result = asyncio.run(amazon_search(search_query))
        result["gemini_used"] = bool(os.environ.get("GEMINI_API_KEY"))
        return jsonify(result)
    except RuntimeError as exc:
        return jsonify(error=str(exc)), 502
    except Exception:
        app.logger.exception("Unexpected search failure")
        return jsonify(error="An unexpected error occurred while searching Amazon."), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
