##Write a program that initializes a list of books available in a library. Take the name of a
##book as input from the user and check if it is available in the library using membership
##operators (in, not in). Print a message indicating whether the book is available or not.

library = ["Math", "Science" , "Social"]

is_math_in_books = "Math" in library
is_science_in_books = "Science" in library
is_social_in_books = "Social" in library
is_science_not_in_books = "Science" not in library
is_math_not_in_books = "Math" not in library
is_social_not_in_books = "Social" not in library


print(f'"Math" in library : {is_math_in_books}')
print(f'"Science in library : {is_science_in_books}')
print(f'"Social" in library : {is_social_in_books}')
print(f'"Math" not in library : {is_math_not_in_books}')
print(f'"Science" not in library : {is_science_not_in_books}')
print(f'"Social" not in library : {is_social_not_in_books}')
