# 20] Write a Python function that takes a list of words and returns the length of the longest one.
list1=[]
n=int(input("How many wword do you want to enter in list = "))
for i in range(n):
      word=input("Enter the word = ")
      list1.append(word)
      i+=1
print("list = ",list1)
check=max(list1,key=len)
print("longest word in list ",check," and length is ",len(check))
