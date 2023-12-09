# 8] Write a python program to find the longest words.
# Open the file named "module3.2.txt" in read mode
f1 = open("module3.1.txt", "r")
# Read the entire content of the file
read_file = f1.read()
# Split the content into a list of words
words = read_file.split()
# Print the list of words
print("words =", words)
# Find and print the longest word in the list
longest_word = sorted(words,key=len)
print("The longest word is:", longest_word[-1])
# Close the file to free up system resources
f1.close()

