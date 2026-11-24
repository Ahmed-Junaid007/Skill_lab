#BOOLEAN
'''print(bool(0.0))
print(int(True))'''
#COMPLEX_NUMBERS
'''a=2+7j
print(a)
a=2+7J
print(a)
'''
#SET
"""a={40,10,12,30,1}"""
'''print(a,type(a))'''
'''print(a[0])'''
'''a={(10,20)}
print(a)'''
'''a={'a':[10,20,30],'b':40}
print(a['a'][1])
print(a['a'][-2])
print(list(a.values())[0][1])'''
#STRING SLICING
'''a="ahmed"'''
'''print(a[2:3:1])'''
'''print(a[2:3+1:1])'''
'''print(a[1:2:1])'''
'''print(a[-3:-2+1])'''
'''a="Good Morning"'''
'''print(a[7:11])'''
"""print(a[-5:-1])"""
'''a='AHMED'''
'''print(a[3:0:-1])'''
"""print(a[-2:-5:-1])"""
'''print(a[-1:-6:-1])'''
'''print(a[-3:-6:-1])'''
'''print(a[1:5+1:2])'''
'''print(a[5::3])'''
'''print(a[5:11+1:3])'''
'''print(a[-7::3])'''
'''print(a[-4:-6:-1], ' ')'''
'''print(a[-2:-8-1:-3])
print(len(a[-2:-8-1:-3]))'''
#INPUT STATEMENTS
'''a=int(input("enter:"))
print(a)
print(type(a))'''
'''a= eval(input("enter:"))
print(a)
print(type(a))'''
#CONDITIONAL STATEMENTS
'''a = int(input('Enter a number'))
if a%2==0 :
    print('even')
else:
    print('odd')'''
'''a = eval(input('Enter the list:'))
if len(a)== 5:
    print('The length of the list is 5')
else:
    print("The length of the list is not 5")'''
#ASCII VALUES
'''print(ord('a'))'''
'''print(ord('z'))'''
'''print(ord('Z'))'''
'''print(ord('A'))'''
'''print(chr(65))'''
'''print(chr(97))'''
'''print(chr(ord('a')-32))'''#converting lowercase to uppercase
'''print(chr(ord('A')+32))'''#converting uppercase to lowercase
'''ch = input('enter:')
if 'A' <= ch <= 'Z':
    print("It is in uppercase")
elif "a" <= ch <= "z":
    print("It is in lowercase")
else:
    print("The character is not a letter")'''#checking if the charecter is in uppercase or lowercase and also if its a letter or not
#NESTED IF STATEMENTS
'''user_name=input('enter user name:')
user_password=input('enter password:')
if user_name == 'Ahmed1907':
    if user_password == 'Ahmed@1907':
        print("Login Successfull!!")
    else:
        print("Wrong Password!")
else:
    print("Wrong user name!")'''#checking user name and password using nested if statements
#LOOP STATEMENTS
'''i =1
while i <= 100 :
    print(i)
    i += 1'''#printing numbers till 100
'''i=1
while i <= 50:
    if i%2==0:
        print(i)
    i += 1'''#printing even numbers till 50
'''for i in range(51):
    if i%2==0:
      print(i)'''#printing even numbers till 50 using for loop
'''i=2
while i<=50:
    print(i)
    i+=2'''#printing even numbers till 50
'''n=int(input('enter num:'))
rev = 0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print(rev)'''#reversing a number without typecasting
'''n = input('enter a num:')
m = n[::-1]
print(m)'''#reversing a number with typecasting
'''for i in range(1,101):
    print(i)'''
'''l=[10,20,30]
for i in l:
    print(i)'''#printing elements of a list using for loop
'''s=input('Enter:')
rep=''
for i in s:
    if "A" <= i <= "Z":
        rep+= chr(ord(i)+32)
    elif "a" <= i <= "z":
        rep+=chr(ord(i)-32) 
    else:
        rep+= i
print(rep)'''#converting uppercase to lowercase using for loop
'''s=input('Enter:')
rev=''
for i in s:
    rev=i+rev
print(rev)'''#reversing a string using for loop
'''for i in range(1,6):
    for j in range(1,6):
         print('*',end=' ')
    print()'''#printing a square pattern of stars
'''for i in range(1,6):
    for j in range(1,6):
         if i==j:
              print('1',end=' ')
         else:
              print('@',end='  ')
    print()'''#printing a square pattern of 1 and @
for i in range(1,6):
    for j in range(1,6):
        if i>j:
            print('0',end=' ')
        else:
            print('1',end=' ')
    print()