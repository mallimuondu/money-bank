
print('--------------------------------------')
print('A. Check new account')
print('B. add money')
print('--------------------------------------')
s = input("chose")
if s == 'a':s
    while True:
        username  = input("enter your name: ")
        if not username.isalpha():
            continue
        else:
            try:
                passwored = int(input("enter password: "))
                c.execute("INSERT INTO number(passwored,bankAccountNumber) VALUES(?,?)",(passwored,bankAccountNumber))
            except ValueError:
                print("sorry i did'nt understand that")
        c.execute("INSERT INTO names(username,passwored) VALUES(?,?)",(username,passwored))
        conn.commit()
        print("SUCCESSFULLY ADDED")
        break