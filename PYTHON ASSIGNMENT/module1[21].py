# 21] Write a Python function to reverses a string if its length is a multiple of 4.
string=input("Enter the String = ")
if len(string) % 4 == 0:
    print("reversed string = ",string[-1:-5:-1])
else:
    print("string = ",string)
