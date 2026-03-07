data={"gantedi.srinidhi@gmail.com": 12345,"pandu123@gmail.com":67890,"sravanthi123@gmail.com":45678}
print("......HI, WELCOME TO CODEGNAN.....")
select=int(input("ENTER ONE IF ALREADY REGISTERED / TWO FOR NOT : "))

if select == 1:
  print("....Go to Login Page.....")
  email = input("Enter your email id:  ")
  password = int(input("Enter your password: "))
  
  if email in data and data[email] == password :
      print(" LOGIN IS SUCCESSFULL ")
      
  else:
      print("LOGIN IS FAILED \nENTER THE CORRECT DATA")
elif select == 2:
    print(".....welcome to registration page....")
    email = input("Enter your new email id: ")
    pwd = int(input("Enter your pwd: "))

    if email in data :
        print("Login is failed/n {email} is already exist")
    else:
        data[email] = pwd
        print(" Registration is successfully done ")
else:
    print("Enter the valid choice")
      
             
