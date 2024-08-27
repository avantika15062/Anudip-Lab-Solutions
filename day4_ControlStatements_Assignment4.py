#Create a Python program that checks if a user-given number is positive, negative, or zero.
num=int(input("Please enter the number : ")) #taking input from user
if num > 0 :                   # condition to check if number is positive
    print("The number is positive")
elif num < 0:                   #condition to check if number is negative
    print("The number is negative")
elif num == 0:
    print("The number is zero")
    
#answer
"""
Please enter the number : 5
The number is positive
"""
