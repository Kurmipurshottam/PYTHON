# 7] Write a Python program to remove duplicates from a list.
list1=[1,2,3,4,5,6,7,6,3,5,2]
list2=[]
print("with duplicates value = ",list1)
#loop on list1
for i in list1:
    if i not in list2:
        list2.append(i)
print("with out duplicates value = ",list2)
    
