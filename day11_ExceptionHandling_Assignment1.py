#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.


def div_nums(a,b): #define a function and pass parameters as a and b
    try:         # create a try and except block
        result = a/b #divide the parameters and store in variable result
        print(f"The answer after division is  : {result}") #print the result

    except ZeroDivisionError:  #handle the exception if the denominator is zero
        print("Error!Division by zero is not allowed") #print the error statement if the number is divided by zero

num1 = int(input("Enter the numerator : ")) # take input from user for numerator 
num2 = int(input("Enter the denominator : "))  # take input from user for denominator 
div_nums(num1,num2) # call the function 


'''

answer
Enter the numerator : 4
Enter the denominator : 0
Error!Division by zero is not allowed

'''
