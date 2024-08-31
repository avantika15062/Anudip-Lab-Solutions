#Python program to check if a given number is an Armstrong number

def armstr(a):  #definig the function
    digits = str(a) #converting the function parameter to string to iterate
    num_digits = len(digits) #this will be the power to which each digit will be raised

    sum_of_powers = 0 #initialising the sum of powers to 0
    for digit in digits:   #loop through each digit in the parameter
         sum_of_powers+= int(digit)**num_digits  #convert digit to integer and raise it to the power of length of the digits

    return a == sum_of_powers  #return if parameter is equal to sum of powers
num=int(input("Enter the number :")) #take input from user
if armstr(num):   #use if statement to call the function and check if the number is armstrong or not
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")
    
   
#answer
"""

Enter the number :153
153 is an armstrong number

"""
