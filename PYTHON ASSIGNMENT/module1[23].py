# 23] Write a Python program to insert a string in the middle of a string.
string=input("Enter the string = ")
string1=input("enter the string that you want to enter = ")
print(len(string))
half=int(len(string)/2)
new_string=string[0:half]+string1+string[half:len(string)]
print("After adding string = ",new_string)
