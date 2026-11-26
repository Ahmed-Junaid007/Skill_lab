# Gemini + Playwright Amazon India Search

This project keeps Playwright browser automation. A single HTML file cannot launch Chromium or run Playwright; the HTML frontend therefore communicates with a local Python Flask backend.

## Requirements
- Python 3.10+
- Internet connection
- Optional Gemini API key (without it, Playwright searches the exact text entered)

## Install on Windows (PowerShell)
Open this folder in VS Code, then run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

If Playwright reports missing system/browser dependencies on Linux, run:
```bash
playwright install-deps chromium
```

## Optional: enable Gemini request refinement
Set your API key in the same terminal before starting the app:

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

Optional model override:
```powershell
$env:GEMINI_MODEL="gemini-2.5-flash"
```

Gemini is used to convert a natural-language shopping request into a concise Amazon search phrase. If no API key is configured, the app skips Gemini and searches the entered text directly.

## Run
```powershell
python app.py
```

Open:
http://127.0.0.1:5000

## Notes
- Playwright launches headless Chromium, opens Amazon India, fills the site's search box, submits the search and extracts product title, price, rating and link.
- Amazon may show CAPTCHA/bot checks, rate-limit automated traffic, or change its page markup. This can prevent extraction even when Playwright is installed correctly.
- Use responsibly and comply with Amazon's terms and applicable site rules.
- Do not publish your Gemini API key or commit it to source control.
