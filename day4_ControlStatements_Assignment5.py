#Write a Python program that determines the largest of three numbers entered by the user.
num1=int(input("Enter the first number : ")) #taking input from user for comparing 3 numbers
num2=int(input("Enter the second number : "))
num3=int(input("Enter the third number : "))
if num1 >= num2 and num1 >= num3:     #condition for checking if num1 is the greatest
    print(num1, "is the greatest")
elif num2 >= num1 and num2 >= num3:  #condition for checking if num2 is the greatest
    print(num2, "is the greatest")
else:                                 #else printing num3 is the greatest if above conditions are false
    print(num3, "is the greatest")

#answer
"""
Enter the first number : 12
Enter the second number : 4
Enter the third number : 7
12 is the greatest

"""
