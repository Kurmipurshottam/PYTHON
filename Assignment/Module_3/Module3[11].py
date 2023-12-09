# 11] Write a Python program to write a list to a file.
# List of strings
list1 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen']
# Open the file in write mode
f1 = open("module3.3.txt", "w")
# Write each element of the list to the file with a newline character
for i in list1:
    f1.write(f'{i}\n')
# Print a success message
print(": : List written into a file successfully : : ")
# Close the file
f1.close()

    
