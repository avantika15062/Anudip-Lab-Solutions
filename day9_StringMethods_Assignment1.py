'''
Write a Python program to Count all letters, digits, and special symbols from the given string

 Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3
 '''


def count_all(input_string): #creating a function
    chars = digits = symbols = 0   #initialising variables to 0
    
    for char in input_string: #iterating over each element
        if char.isalpha(): #using isalpha to check if character is alphabet
            chars += 1  #if condition is true chars is incremented by counter 1
        elif char.isdigit():  #using isdigit to check if character is digit
            digits += 1 #if condition is true digits is incremented by counter 1
        else:
            symbols += 1 #if both above conditions are false symbols is incremented by 1
    
    return chars, digits, symbols #returning all the initialised variables

input_string = "P@#yn26at^&i5ve"
chars, digits, symbols = count_all(input_string) #calling the funtion 

print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")

"""
answer
Chars = 8
Digits = 3
Symbols = 4
"""

        
            
            
