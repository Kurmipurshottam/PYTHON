# 12] Write a Python program to copy the contents of a file to another file.
# Open the first file ("module3.3.txt") in read mode
f1 = open("module3.3.txt", "r")
# Read the contents of the first file
f1_data = f1.read()
# Close the first file
f1.close()
# Open the second file ("module3.2.txt") in append mode
f2 = open("module3.2.txt", "a")
# Write the contents of the first file into the second file
f2.write(f1_data)
# Print a message indicating that the contents were successfully copied
print(": : copy the contents of a file to another file successfully : : ")
# Close the second file
f2.close()
