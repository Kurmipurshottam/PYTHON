'''
10] Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.
'''
list1=[]
squre=[]
for i in range(1,31):
    list1.append(i)
    squre.append(i*i)
print("list = ",list1)
#display squre of first five element
print("First five element squre = ",squre[:5])
#display squre of last five element
print("Last five element squre = ",squre[-5:])
