accounts = {}

for i in range(5):
    print(f"\nRegistration {i+1}")
    
    email = input("Enter email: ")
    password = input("Enter password: ")


    if email in accounts:
        print("Email already existed!")
    else:
        accounts[email] = password
        print("Account created successfully!")

print("\n---- Registered Accounts ----")
for email in accounts:
    print(email)
