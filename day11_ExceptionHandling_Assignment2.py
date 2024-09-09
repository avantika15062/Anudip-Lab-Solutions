#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def is_int(): #define a function to check if integer is valid 
    try:   #creating a try block to check if number is integer or not 
        user_input = input("Enter an integer : ") #taking user input
        num = int(user_input) # converting input to an integer 
        print(f" Number entered : {num} is valid") #printing the valid integer number 

    except ValueError: #handling the  value error exception 
          print (f"Error: {user_input} is not a valid integer.") #printing if the number entered is not valid
is_int() #calling the function 


'''
answer
Enter an integer : 2/7
Error: 2/7 is not a valid integer.
'''
