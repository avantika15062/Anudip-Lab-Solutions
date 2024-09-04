'''
Write a Python program to remove duplicate characters of a given string.

 Input = “String and String Function” Output: String and Function
'''

def remove_duplicates(input_string): #defining the funtion
    result= [] #creating a list to store characters without duplicates
    seen = set() #this is a set to keep track of characters already added to the result.

    for char in input_string: #iterating over each character in the input string
        if char not in seen: # if character is not in seen it is added to both seen and result
            seen.add(char)
            result.append(char)

    return ''.join(result) #joining the list into a single string and returning it
input_string = "String and String Function"
output_string = remove_duplicates(input_string) #calling the funtion 

print("Output :", output_string)
     
'''
answer
Output : String adFuco
'''
