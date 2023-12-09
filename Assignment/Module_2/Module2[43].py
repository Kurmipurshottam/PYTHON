'''
43]  Why Do You Use the Zip () Method in Python?
 ->   The zip() function in Python is used to combine two or more iterable dictionaries into
        a single iterable, where corresponding elements from the input iterable are paired together
        as tuples. When using zip() with dictionaries, it pairs the keys and values of the dictionaries
        based on their position in the dictionary.
'''
#Example
list1 = [1, 2, 3, 4]
list2 = ['raj', 'nikhil', 'smit', 'purshottam']
# Use the zip function to combine the two lists into a dictionary
dict1 = dict(zip(list1, list2))
# Print the resulting dictionary
print("Two lists combined into a dictionary:", dict1)

