## Create a set of your favourite hobbies. Add a few more hobbies to the set, then remove
##one.Finally, perform a union with another set of hobbies and find the common ones using intersection.

fav_hobbies = {"Playing" , "Dancing" , "Riding"}


fav_hobbies_second = {"Cooking","Hiking","Dancing"}
fav_hobbies.remove("Playing")

all_hobbies = fav_hobbies.union(fav_hobbies_second)
all_hobbies_inter = fav_hobbies.intersection(fav_hobbies_second)
print(f"My favourite hobbies are {all_hobbies}")
print(f"My favourite hobbies are {all_hobbies_inter}")