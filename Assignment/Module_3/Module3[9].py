# 9] Write a Python program to count the number of lines in a text file.
# Open the file in read mode
f1 = open("module3.2.txt", "r")
# Initialize a counter for counting lines
count = 0
# Read all lines from the file 
lines = f1.readlines()
# Iterate through each line 
for i in lines:
    # Increment the counter for each line
    count += 1
# Print the count of lines in the file
print(f'There are {count} number of lines in the file "{f1.name}".')
# Close the file
f1.close()
