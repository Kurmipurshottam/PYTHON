# 4] Write a Python program to read first n lines of a file.
# Get the number of lines to read from user input
n = int(input("How many lines do you want to read at the first = "))
# Open the file named "module3.2.txt" in read mode
f1 = open("module3.2.txt", "r")
# Read and print the specified number of lines from the file
for i in range(n):
    # Read a line from the file and print it 
    print(f1.readline(), end="")
# Close the file to free up system resources
f1.close()

