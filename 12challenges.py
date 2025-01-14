##Write a program that uses assert to check if a person's age is positive.
#using if else :
age = int(input("enter age :"))

if  age >= 0 :
    print(f"Age is Positive")
else :
   print(f"Age can't be negative")
    
##using assert

current_age = -2
assert current_age >=0, "Age can't be negative"
print("after age negative")

