# 16] Write a Python program to check whether a list contains a sub list.
list1 = [1, 2, 3, 4, 5, 6, 7]
sub_list = [7, 4, 6]
count = 0
# Iterate over elements in the sub_list
for i in sub_list:
    # Check each element in list1
    for j in list1:
        # If there is a match, increment the count
        if i == j:
            count += 1
# Check if the count of matching elements is equal to the length of the sub_list
if count == len(sub_list):
    print(": : list contains a sub list : :")
else:
    print(": : list does not contain a sub list : :")

