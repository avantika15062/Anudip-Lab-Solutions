''' Write a Python program to reverse words in a string 

String = “Deeptech Python Training” '''

# Given string
string = "Deeptech Python Training"

# Split the string into words
words = string.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed list of words into a single string
reversed_string = " ".join(reversed_words)

# Print the result
print(reversed_string)


'''
answer
Training Python Deeptech
'''
