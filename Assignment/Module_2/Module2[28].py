# 28]  Write a Python program to remove an empty tuple(s) from a list of tuples.
list1=[(1,2,3,4),(),(5,6),(),(7,8,9),(),(),(10,)]
print("list with empty tuple = ",list1)
list2=[]
# Iterate through each tuple in list1
for i in list1:
    # Check if the tuple is not empty
    if i != ():
        # Append the non-empty tuple to list2
        list2.append(i)
# Display the list without empty tuples
print("list without empty tuple =", list2)
