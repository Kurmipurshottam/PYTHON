'''
1] What is File function in python? What is keywords to create and write file.
-> the file function is allows to make a file for write in a file or read from a file.
-> The open() function is used to open and create the file and write() method
     used to write data in the file.
'''
# Opening a module3.1.txt file in write mode ("w")
file = open("module3.1.txt", "w")
# Writing content to the file
file.write("Hello! I am Purshottam\n")
# Printing a message the file has been created and written successfully
print(": : File created and written successfully : :")
# Closing the file to release system resources
file.close()
