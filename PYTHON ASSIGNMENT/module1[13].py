# 13]  Write a Python program to count the number of characters (character frequency) in a string.
name=input("Enter any character that frequency you want = ")
count={}
for i in name:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("Frequency of character = ",count)
