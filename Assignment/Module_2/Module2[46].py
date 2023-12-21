'''
46] Write a Python program to combine values in python list of dictionaries.
       Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
       300}, o {'item': 'item1', 'amount': 750}]
       Expected Output:
       Counter ({'item1': 1150, 'item2': 300})
'''
sample_data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]
combined_values = {}  # Initialize an empty dictionary to store combined values
# Iterate through each dictionary in the sample_data list
for i in sample_data:
    item = i['item']  # Extract the 'item' key from the dictionary
    amount = i['amount']  # Extract the 'amount' key from the dictionary
    # Check if the 'item' key already exists in the combined_values dictionary
    if item in combined_values:
        combined_values[item] += amount  # If exists, add the 'amount' to the existing value
    else:
        combined_values[item] = amount  # If not, create a new key-value pair
print(combined_values)
