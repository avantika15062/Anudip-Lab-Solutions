#Python program to check if the given string is a palindrome 
def palindrome(a): #define a function
    a=a.lower().replace(' ','')  # Convert string to lowercase and remove spaces
    reversed_string = ''  # Initialize an empty string for the reversed string
    for i in range (len(a),0,-1):  # Loop through the string in reverse order
        reversed_string += a[i-1] # Append each character to the reversed_string

    return a == reversed_string  # Check if the original string is equal to the reversed string
x=str(input("Enter the string :")) #taking input from user
if palindrome(x):  #checking through if condition of the input from user is a palindrome or not
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")

#answer
"""

Enter the string :Madam
Madam is a palindrome

"""
