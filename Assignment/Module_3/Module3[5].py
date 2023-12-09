# 5] Write a Python program to read last n lines of a file.
# Get the number of lines to read from user input
n = int(input("How many lines do you want to read at the last = "))
# Open the file named "module3.2.txt" in read mode
f1 = open("module3.2.txt", "r")
# Read all lines from the file and store them in a lines
lines = f1.readlines()
# Print the last n lines 
for line in lines[-n:]:
    print(line, end="")
# Close the file to free up system resources
f1.close()

