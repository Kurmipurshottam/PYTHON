'''
9] Write a Python program to sum of three given integers. However, if two values are equal
sum will be zero.
'''
no1=int(input("Enter number 1 = "))
no2=int(input("Enter number 2 = "))
no3=int(input("Enter number 3 = "))
if no1==no2 or no2==no3 or no3==no1:
    print("Sum = ",0)
else:
    print("Sum = ",no1+no2+no3)
