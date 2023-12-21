'''
47] Write a Python program to create a dictionary from a string.
       Note: Track the count of the letters from the string.
       Sample string: 'w3resource'
       Expected output:
       {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''
input_string = 'purshottam'
# Initialize an empty dictionary to store the letter counts
string_count = {}
# Count occurrences of each letter in the string
for i in input_string:
    if i in string_count:
        string_count[i] += 1
    else:
        string_count[i] = 1
# Display the resulting dictionary
print("dictionary = ",string_count)
