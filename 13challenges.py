##Write a program that finds the total and average of the following list:
##expenses = [889,788,5656,4455,455,45]



expenses = [889,788,5656,4455,455,45]
total = 0
for price in expenses :

       total +=price 
       average = total / len(expenses)
       
       
       
print(f"Total : , {total}")
print(f"Average : , {average:.2f}")












    