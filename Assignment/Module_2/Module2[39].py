# 39] Write a Python script to merge two Python dictionaries.
# Define the first dictionary
dict1 = {1: 'raj', 2: 'smit', 3: 'nikhil'}
# Define the second dictionary
dict2 = {4: 'purshottam'}
# Print the original dictionaries
print("dict1 = ", dict1)
print("dict2 = ", dict2)
# Merge dict2 into dict1 using the update method
dict1.update(dict2)
# Print the merged dictionary
print("merge dictionaries = ", dict1)

