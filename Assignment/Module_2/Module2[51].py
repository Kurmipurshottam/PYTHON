# 51] Write a Python function that checks whether a passed string is palindrome or not.
def palindrome(name):
    if name[0:] == name[::-1]:
        # Check if the first and last characters of the name are the same.
        print("String is a palindrome.")
    else:
        print("String is not a palindrome.")
# Taking user input for the naame
name = input("Enter a name = ")
# Calls the 'palindrome' function with the user-inputted string.
palindrome(name)

