# 7] Write a Python program to read a file line by line store it into a variable.
# Open the file named "module3.2.txt" in read mode
f1 = open("module3.2.txt", "r")
# Read all lines from the file and store them in a variable
read_line_by_line = f1.readlines()
# Print the list of lines
print("print through variable = ",read_line_by_line)
# Close the file to free up system resources
f1.close()
