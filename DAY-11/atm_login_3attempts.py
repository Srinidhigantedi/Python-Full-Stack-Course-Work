for i in range(3):
    username=input("enter the username:")
    password=input("enter the password:")
    if username=='admin' and password=='PFS48':
        print("Login Successful")
        break
else:
    print("Account Locked")  
