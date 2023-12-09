# 49]  Write a Python function to check whether a number is in a given range.
def check_range(no):
    # Check if the number is in the range [1, 5]
    if no in range(1, 5):
        print(f': : {no} is in the range : :')
    else:
        print(f': : {no} is out of the range : :')
# Take user input for the number
no = int(input("Enter a number to check if it's in the range or not = "))
# Call the check_range function with the user-input number
check_range(no)

