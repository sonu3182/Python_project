from random import *
user_pass=input("enter your password")
password=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guess=""
c=0
while(guess !=user_pass):
    guess=""
    for letter in range(len(user_pass)):
        guess_letter=password[randint(0,25)]
        guess=str(guess_letter)+str(guess)
    c=c+1
    print(guess)
print(c)
print("your password is ",guess)