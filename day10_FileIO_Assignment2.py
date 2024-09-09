# Write a function in Python to count and display the total number of words in a text file “ABC.txt”
def count_words():
    
        # Open the file in read mode
        with open('ABC.txt', 'r') as file:
            # Initialize a counter for the words
            word_count = 0
            
            # Loop through each line in the file
            for line in file:
                # Split each line into words and add the count of words in the line
                words = line.split()
                word_count += len(words)
                
            # Display the total word count
            print(f"Total number of words: {word_count}")

count_words()
   
'''

answer
Total number of words: 35

'''
