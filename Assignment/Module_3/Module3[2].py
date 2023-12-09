# 2] Write a Python program to read an entire text file.
# Opening a module3.1.txt file in read mode ("r")
file = open("module3.1.txt", "r")
# Reading the content of the file
read_data = file.read()
# Printing the content of the file
print("After reading, data is = ", read_data)
# Closing the file to release system resources
file.close()
