'''
22] Write a Python program to get a string made of the first 2 and the last2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.
'''
str1=input("Enter the string = ")
if len(str1)<2:
    print(" : : Empty string : : ")
else:
    print("First two character and last two charaacter of string : : ",str1[0:2]+str1[-2:])

