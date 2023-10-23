'''
10] Write a Python program that will return true if the two given integer values are equal or
their sum or difference is 5.
'''
no1=int(input("Enter the number 1 = "))
no2=int(input("Enter the number 2 = "))
if no1 == no2 or abs(no1-no2) == 5 or (no1+no2) == 5:
    print("true")
else:
    print("False")
