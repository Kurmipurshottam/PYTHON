# 22] Write a Python program to check whether an element exists within a tuple.
tuple1=(1,9,2,8,5,6,7,4,3)
print("tuple1 = ",tuple1)
# taking input to user
n=int(input("enter number that you want to check in tuple exists or not = "))
if n in tuple1:
    print(": : element exists in tuple1 : :")
else:
    print(": : element can not exists in tuple1 : :")
