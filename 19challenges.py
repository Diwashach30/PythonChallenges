##1. Write a program that takes a list of numbers and creates a new list containing the
##squares of all even numbers from the original list.
##2. Write a program that takes a dictionary of student names and their grades, and creates a
##new dictionary containing only the students who passed the exam (grade 50 or above).


list_of_numbers = [x for x in range(1,11)]
print(f"List of numbers is {list_of_numbers}")

list_of_even = [ x**2 for x in list_of_numbers if x%2 ==0]
print(f"List of square of even number is {list_of_even}")


stud_dict  = {"Sharad" : 58 , "Nabin" : 48 , "Sudip" : 59}

passed_stud = {name : score for name, score in stud_dict.items() if score > 50}
print(f"Following students are passed  : {passed_stud}")