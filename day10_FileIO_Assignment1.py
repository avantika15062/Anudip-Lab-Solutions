# Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
def read_file():
    with open('ABC.txt', 'r') as file:  # Open the file "ABC.txt" in read mode
        for line in file :   # Iterate through each line in the file
            print (line.strip()) # strip() removes any leading/trailing whitespace characters
    

read_file() # Call the function to read and display the file content


'''

answer
Hello, this is a sample text file.
It contains multiple lines of text.
Each line will be read and processed.
Python is a powerful programming language.
This is the last line of the sample file.

'''
