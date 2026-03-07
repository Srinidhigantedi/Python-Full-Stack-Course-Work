data = {
    123456 : {'pin':1234,'balance':5000,'history':[]},
    234561 : {'pin':2341,'balance':10000,'history':[]},
    345612 : {'pin':3423,'balance':7000,'history':[]}
}

def check_balance(acc):
    print(f"Your Balance Amount is ${data[acc]['balance']}")

def deposit(acc):
    amount = int(input("Enter the amount: "))
    data[acc]['balance']+=amount
    data[acc]['history'].append(f"{amount} is deposited")
    print(f"{amount} is deposited successfully")

def withdraw(acc):
    amount = int(input("Enter the amount: "))
    if amount<=data[acc]['balance']:
        data[acc]['balance']-=amount
        data[acc]['history'].append(f"{amount} is Withdraw")
        print(f"{amount} is withdraw successfully")
    else:
        print("You don't have enough balance")


def view_history(acc):
    if  data[acc]['history']:
        print("-------Transaction History---------")
        for i in data[acc]['history']:
            print(i)
        else:
            print("--------End of history-------")
    else:
        print("No Transactions")
        def Set_Pin(acc)
        set_pin=data[acc]["pin"]
        

        
def menu():
    print('1.Check Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.Set Pin')
    print('5.View Transactions')
    print('6.Exit\n')

print("Welcome to the ATM")

acc = int(input("Enter the account number: "))
pin = int(input("Enter the pin: "))

if acc in data and data[acc]['pin']==pin:
    print("Login Successful")
    while True:
        menu()
        ch = int(input("Enter the choice: "))
        if ch==1:
            check_balance(acc)
        elif ch==2:
            deposit(acc)
        elif ch==3:
            withdraw(acc)
        elif ch==5:
            view_history(acc)
        elif ch==6:
            print("Thankyou")
            break
else:
    print("Invalid Login. Try Again")
        
    
    
