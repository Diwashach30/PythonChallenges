##Write a program that takes the age and citizenship status of a person as input from the
##user. Use logical operators (and, or, not) to determine if the person is eligible to vote
##(age >= 18 and is a citizen). Print an appropriate message based on the result.

age = int(input("Enter the age : "))



if age > 18 :
     print (f"A person is eligible to vote and citizen of his/her country.")
elif age > 16 < 18 :
     print (f"A person is citizen of his/her country but isnot eligible to vote.")
else :
    print (f"A person is neither citizen nor eligble to vote.")
   
     