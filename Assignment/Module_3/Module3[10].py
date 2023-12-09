# 10] Write a Python program to count the frequency of words in a file.
# Open the file in read mode
f1 = open("module3.1.txt", "r")
# Read the content of the file
r_word = f1.read()
# Split the content into words
words = r_word.split()
# Print the list of words
print(words)
# Initialize an empty dictionary for word frequency
frequency = {}
# Count the frequency of each word
for i in words:
    # Check if the word is already in the dictionary
    if i in frequency:
        frequency[i] += 1
    else:
        # If the word is not in the dictionary, add it with a frequency of 1
        frequency[i] = 1
# Print the word frequency
print(" : : Frequency of each word : : ")
for i,j in frequency.items():
    print(f'"{i}" word frequency is = {j}')
# Close the file
f1.close()
