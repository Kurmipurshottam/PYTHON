# 16] Write a Python program to count the occurrences of each word in a given sentence.
sentance=input("Enter any statment = ")
count=dict()
words=sentance.split()
for i in words:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("occurrences of word is = ",count)

