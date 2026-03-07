balance=10000
while True:
    amount=int(input("enter the amount :"))
    if amount==0:
        print("Thank You")
        break
    if amount<=balance:
        print(f"{amount} withdraw sucessfully")
        balance-=amount
        print(f"current balance :{balance}")
    else:
        print("Insuffient Balance")
