##Create a Python program that asks the user for their birthdate (in YYYY-MM-DD format) and
##calculates their age.

import datetime

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birth_date = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
current_date = datetime.datetime.now()

age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

print(f"You are {age} years old.")