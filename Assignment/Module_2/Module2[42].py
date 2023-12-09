# 42] Write a Python program to print all unique values in a dictionary.
dict1 = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 4, 'g': 1}
print("Original dictionary:", dict1)
# Create an empty dictionary to store unique values along with their corresponding keys
dict2 = {}
# Iterate through the key-value pairs in dict1
for key, value in dict1.items():
    # Check if the current value is not already present in the values of dict2
    if value not in dict2.values():
        # If the condition is true, add the key-value pair to dict2
        dict2[key] = value
# Print the resulting dictionary with unique values and their corresponding keys
print("Dictionary with unique values:", dict2)


