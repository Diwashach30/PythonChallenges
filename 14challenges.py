##Write a program that calculates the total and average of the following list of numbers, stopping if
##a negative value is encountered (using break), and skipping any zero values (using continue).
##values = [10, 0, 25, 0, 50, -1, 40]


values = [10, 0, 25, 0, 50, -1, 40]
total = 0 
count = 0
for value in values :
    if value < 0 :
      break
    if value == 0 :
        continue
    total += value
    count += 1
if count > 0:
    average = total / count
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
else:
    print("No valid values to calculate average.")
    
 