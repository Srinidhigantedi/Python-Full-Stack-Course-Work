def atm_withdraw():
    amount = int(input("Enter amount to withdraw: "))

    
    if amount <= 0:
        print("Invalid amount!")
        return

    denominations = [2000, 500, 200, 100, 50, 20, 10]
    notes_count = {}

    for note in denominations:
        count = amount // note
        if count > 0:
            notes_count[note] = count
            amount = amount % note

    if amount != 0:
        print("Amount cannot be dispensed completely with available denominations.")
    else:
        print("\nWithdrawn successfully! Denominations given:")
        for note, count in notes_count.items():
            print(f"{note} x {count}")

atm_withdraw()
