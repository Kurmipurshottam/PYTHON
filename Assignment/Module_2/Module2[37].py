# 37] Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
# Display a message
print("====print a dictionary where the keys are numbers between 1 and 15====")
# Take user input for the range
r = int(input("Enter the range = "))
# Initialize an empty dictionary
dict1 = {}
# Loop through numbers from 1 to the specified range
for i in range(1, r + 1):
    # Assign square of the number as the value for each key
    dict1[i] = i * i
# Print the resulting dictionary
print("dictionary =", dict1)

