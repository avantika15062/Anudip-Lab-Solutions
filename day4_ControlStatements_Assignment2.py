# Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
age=int(input("Enter your age please : ")) #taking the age input from user
if age >= 18:                              #if condition to check if age is greater than or equal to 18
    print("Yes,you are eligible to vote")   #printing this if condition is ture
else:
    print("Sorry,you cannot vote.")          #printing this if condition is false
    
#answer
"""
Enter your age please : 15
Sorry,you cannot vote.
"""
