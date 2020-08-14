from daterbase import *
import random
print('--------------------------------------')
print('A. Check new account')
print('B. add money')
print('--------------------------------------')
s = input("chose: ")
if s == 'a':
    while True:
        username  = input("enter your name: ")
        if not username.isalpha():
            continue
        else:
            try:
                passwored = int(input("enter password: "))
#                c.execute("INSERT INTO number(passwored,bankAccountNumber) VALUES(?,?)",(passwored,bankAccountNumber))
            except ValueError:
                print("sorry i did'nt understand that")
        c.execute("INSERT INTO names(username,passwored) VALUES(?,?)",(username,passwored))
        bankAccountNumber = random.randint(1000,100000)
        print(bankAccountNumber)
        print("THIS IS YOUR BANK ACCOUNT NUBER")
        conn.commit()
        print("SUCCESSFULLY ADDED")
        break
elif s == 'b':
    amount = 0
    d = int(input("inter the amount you want: "))
    total = amount + d
    print(total)
    c.execute("INSERT INTO money VALUES(?)",(total))