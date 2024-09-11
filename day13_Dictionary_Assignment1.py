# Write a Python program and calculate the mean of the below dictionary.
#test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

 # Given dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the mean
mean_value = sum(test_dict.values()) / len(test_dict)

# Output the mean
print(f"The mean of the values in the dictionary is: {mean_value}")

'''
answer
The mean of the values in the dictionary is: 6.2
'''

