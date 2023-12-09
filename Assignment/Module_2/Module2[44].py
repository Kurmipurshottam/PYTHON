'''
44] Write a Python program to create and display all combinations of letters,
       selecting each letter from a different key in a dictionary.
       Sample data: {'1': ['a','b'], '2': ['c','d']}
       Expected Output:
       ac ad bc bd
'''
dict1 = {1: ['a', 'b'], 2: ['c', 'd']}
# Print the original dictionary
print("dictionary = ", dict1)
# Iterate over the elements in the list associated with key 1
for i in dict1[1]:
    # Iterate over the elements in the list associated with key 2
    for j in dict1[2]:
        # Print the concatenation of the current elements from both lists
        print(i + j, end=' ')

