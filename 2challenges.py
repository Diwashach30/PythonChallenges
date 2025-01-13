##Write down what you spend each day from Sunday to Saturday,
## add them up to find the total for
##the week, and figure out the average amount spent per day.
 
##List of Expenses
Sunday = int("500")
Monday = int("300")
Tuesday = int("700")
Wednesday= int("100")
Thursday = int("900")
Friday= int("390")
Saturday = int("350")

total = Sunday + Monday + Tuesday + Wednesday + Thursday + Friday + Saturday

average = total / 7

print(f"Total expenses of week is {total}.")
print(f"Average amount spent per day is {average:.2f}.")

