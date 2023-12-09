# 3] Write a Python program to append text to a file and display the text.
# Open the file "module3.1.txt" in append mode ("a").
f1 = open("module3.1.txt", "a")
# Write the string "I am BCA student" to the file.
f1.write("I am BCA student\n")
# Close the file to save changes.
f1.close()
# Open the file "module3.1.txt" in read mode ("r").
f2 = open("module3.1.txt", "r")
# Read the contents of the file and store them in the variable read_data.
read_data = f2.read()
# Print a message indicating that the data is being displayed.
print(" : : Data is : : ")
# Print the contents of the file.
print(read_data)
# Close the file after reading its contents.
f2.close()

