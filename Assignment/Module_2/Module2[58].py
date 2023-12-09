# 58]  Write a Python program to read a random line from a file.
import random # Import the random module
# Open the file for reading
f1 = open("question58.txt", "r")
# Read all lines from the file
lines = f1.readlines()
# Choose a random line from the list of lines
random_line = random.choice(lines)
# Print the randomly selected line
print("Random line from file =", random_line)
# Close the file
f1.close()
