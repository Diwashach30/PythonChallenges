##ATM PROJECT

balance = 6900.00

print("Diwash Bank")

while True:
    input_text = """"
Please select an Option
1.Check Balance
2.Deposit Money
3.Withdraw Money 
4.EXIT
:
"""
    choice = int(input(input_text))
    
    if choice == 1:
           print(f"Your current balance is: {balance:.2f}")
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposit Success. Your New Balance is {balance}")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw:"))
        if balance >= amount:
            balance -= amount
            print(f"Withdraw Success. Your New Balance is {balance}")
        else:
            print("Insuffieient Balance")
    elif choice == 4:
        print(f"Thank you for using Diwash Bank")
        break
    else: 
        print("Invalid Choice.Try again")
            