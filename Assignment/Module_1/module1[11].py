# 11] Write a python program to sum of the first n positive integers.
n=int(input("Enter the number where do you get the sum of positive number = "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum of first",n,"positive number is = ",sum)
