# 33] Write a Python script to concatenate following dictionaries to create a new one.
dict1 = {21: 'smit', 75: 'purshottam'}
dict2 = {111: 'nikhil'}
print("Dictionary 1 =", dict1)
print("Dictionary 2 =", dict2)
# Initialize an empty dictionary for concatenation
concatenate_dict = {}
# Loop through each dictionary and update the concatenated dictionary
for item in dict1, dict2:
    concatenate_dict.update(item)
# Print the result after concatenating dictionaries 1 and 2
print("After concatenating dictionaries 1 and 2 =", concatenate_dict)
