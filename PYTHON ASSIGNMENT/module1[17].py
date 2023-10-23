'''
17] Write a Python program to get a single string from two given strings,separated by a space and
swap the first two characters of each string.
'''
first_name=input("Enter first string = ")
last_name=input("Enter second string = ")
print("Seprated two string by space = ",first_name,last_name,sep=" ")
string1=first_name[:2]+last_name[2:]
string2=last_name[:2]+first_name[2:]
print(" : : after swap first two characters : :")
print("First string after change first two charactre = ",string1)
print("Second string after change first two charactre = ",string2)
