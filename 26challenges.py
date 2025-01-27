##Create a Python program that asks the user to input a number. The program should then
##determine if the number is odd or even and display the result. If the user enters a non-numeric
##value, handle the exception and prompt the user to enter a valid number.
try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
finally:
    print("Program execution completed.")
    

