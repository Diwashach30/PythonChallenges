##Write a Python program that takes a user's full name as input and Convert the full name to title
##case (capitalize the first letter of each word). Also remove trailing and leading space.

name = input("Enter full name :")

full_name = name.strip().title()


print(f"User full name is {full_name} ")