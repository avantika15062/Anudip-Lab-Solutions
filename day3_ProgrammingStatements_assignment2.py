#Using input function take two number and then swap the number

num1= int(input("Enter the number 1 : "))#taking input for first number
num2= int(input("Enter the number 2 : "))#taking input for second number
print("The first number is" ,num1, "The second number is ",num2)
temp = num1 # creating a third temporary variable for swapping
num1=num2 
num2 = temp
print("After swapping,value of num1 is", num1 ,"value of num2 is ", num2 )

#answer
"""
Enter the number 1 : 5
Enter the number 2 : 7
The first number is 5 The second number is  7
After swapping,value of num1 is 7 value of num2 is  5

"""
