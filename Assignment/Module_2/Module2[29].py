# 29]  Write a Python program to unzip a list of tuples into individual lists.
list_of_tuples=[(1,2,3,11),(4,5,6,7),(8,9,10,12),(1,4,8,0)]
print("list of tuples = ",list_of_tuples)
list1=[]
list2=[]
list3=[]
list4=[]
# Unzip the list of tuples into separate lists for each position
for i in list_of_tuples:
    list1.append(i[0])
    list2.append(i[1])
    list3.append(i[2])
    list4.append(i[3])
# Display the result after unzipping
print(": : After unzipping list of tuples : :")
print("list1 = ", list1)
print("list2 = ", list2)
print("list3 = ", list3)
print("list4 = ", list4)
