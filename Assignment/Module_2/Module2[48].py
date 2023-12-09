# 48] Write a Python function to calculate the factorial of a number (a nonnegative integer)
def factorial(no):
    # Base case: factorial of 0 is 1
    if no == 0:
        return 1
    # Recursive case: calculate factorial for positive integers
    elif no > 0:
        return no * factorial(no - 1)
    # Handle invalid input (negative number)
    else:
        print(": : invalid input : : ")
        exit()
# Take user input for the number
no = int(input("Enter a number to find factorial = "))
# Print the result using the factorial function
print(f'{no} factorial is = ', factorial(no))

