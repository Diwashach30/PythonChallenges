##Write a program that takes user input for year of birth (as a string) in the format 'YYYY’ and finds
##the age of the person.

##input as a year of birth

birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))

current_age = current_year - birth_year

print(f"The current age of a person is {current_age}")
