# 3] Write a Python program to get the Fibonacci series of given range.
no=int(input("Enter the limit of Fibonacci series = "))
f1=0
f2=1
f3=f1+f2
print("Fibonacci series = ",f1,f2,f3,end=" ")
for i in range(0,no):
    f1=f2
    f2=f3
    f3=f1+f2
    i+=1
    print(f3,end=" ")

