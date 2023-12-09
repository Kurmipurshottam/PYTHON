# 15] Write a Python program to get unique values from a list.
list1=[1,2,3,4,5,4,3,2]
list2=[]
print("list = ",list1)
# loop on list1
for i in list1:
    if i not in list2:
        list2.append(i)
print("unique list = ",list2)
