##1. Create a function that finds a cube of a number.
##2. Create a function that finds age from birth year.


def cube(number): 
    cube = number * number * number

    return cube
print(cube(int(input("Enter a number :"))))


#solution of 2 number

def age(birth_year):
    current_year = 2025
    age = current_year - birth_year

    return age
print(age(int(input("Enter birth year :"))))