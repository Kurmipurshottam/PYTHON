# 27]  Write a Python program to find the repeated items of a tuple.
tuple1 = (1, 2, 3, 4, 5, 6, 2, 3, 4)
list1 = []  
repeated_items = [] 
# Loop through each element in the  tuple1
for i in tuple1:
    # Check if the element is not in the unique list
    if i not in list1:
        # If not, add it to the unique list
        list1.append(i)
    else:
        # If it's already in the unique list, add it to the repeated list
        repeated_items.append(i)
# Convert the unique list to a tuple
tuple2 = tuple(list1)
# Convert the repeated list to a tuple
tuple3 = tuple(repeated_items)
print("Original tuple = ", tuple1)
print("After removing duplicate values from tuple = ", tuple2)
print("Duplicate values from tuple = ", tuple3)
