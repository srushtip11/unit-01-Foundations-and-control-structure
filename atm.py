pin = int(input("Enter PIN: "))

if pin == 1234:

    balance = int(input("Enter balance: "))
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient Balance")

else:
    print("Wrong PIN")
