## Create a tuple of your favorite fruits and display all the fruits.
## Access and print the first and last fruit in the tuple.
## Attempt to change the second fruit in the tuple and observe what happens (this should
##raise an error since tuples are unchangeable).
## Combine this tuple with another tuple of your favorite vegetables, and print the resulting
## combined tuple.
## Find and print the length of the combined tuple using the len() function.


fav_fruits = ("Apple" , "Watermelon" , "Banana" , "Mango")

first_fav_fruits = fav_fruits[0]
last_fav_fruits = fav_fruits[3]
##fav_fruits[2] = "Litchi"  ##ERROR BECAUSE TUPLE IS UNCHANGEABLE

print(f"First fruit is {first_fav_fruits}")
print(f"last fruit is {last_fav_fruits}")


fav_veg = ("Cabbage" , "Cauli" , "Tomato")

combine = fav_fruits + fav_veg
print(f"Combine is {combine}")
length = len(combine)

print(f"Length is {length}")