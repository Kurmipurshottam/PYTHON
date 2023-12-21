'''
17] When is the finally block executed ?
 ->  The code inside the try block is executed. If an exception occurs during the execution
       of the try block, the corresponding except block is executed to handle the exception.
       Regardless of whether an exception occurs or not, the code inside the finally block is executed.
'''
try:
    # Attempt to get user input and perform a division
    x = int(input("Enter x = "))  # Try to convert user input for x to an integer
    y = int(input("Enter y = "))  # Try to convert user input for y to an integer
    result = x / y  # Attempting a division operation
    print("Try block: Division successful. Result =", result)
except ZeroDivisionError:
    # Handling the specific exception when division by zero occurs
    print("Except block: Cannot divide by zero!")
finally:
    # Code to be executed whether an exception occurs or not
    print("Finally block: This will always be executed, regardless of exceptions.")


