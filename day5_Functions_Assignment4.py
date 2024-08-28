#Accept a name from the user and display that in lower case using lower() function.


name=str(input("Please enter your name: ")) #taking input from user
res= str.lower(name)  #using built in function lower to convert the input from capital letters to small letters and storing it in a variable res
print("The entered name in small letters is : ", res)  #printing the variable res



#answer
"""
Please enter your name: AVANTIKA
The entered name in small letters is :  avantika
"""
