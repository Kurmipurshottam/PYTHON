# 14] Write a Python program to find the second smallest number in a list.
list1=[7,0,1,8,1,5,6,4,0,5]
list2=[]
print("list = ",list1)
# if list contain diplication so first delete the duplicaation
# loop on list1
for i in list1:
    if i not in list2:
        list2.append(i)
#print the unique list
print("unique list = ",list2)
# sorted the list in ascending order
list2=sorted(list2)
print("sorted list = ",list2)
print("second smallest number = ",list2[1])
