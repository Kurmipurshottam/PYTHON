'''
17] When is the finally block executed ?
 ->  The finally block is always executed even exception occurred or not. 
'''
try:
    # Attempt to get user input and perform a division
    x = int(input("Enter x = "))  
    y = int(input("Enter y = "))  
    result = x / y  # Attempting a division operation
    print("Try block: Division successful. Result =", result)
except ZeroDivisionError:
    # Handling the specific exception when division by zero occurs
    print("Except block: Cannot divide by zero!")
finally:
    # Code to be executed whether an exception occurs or not
    print("Finally block: This will always be executed, regardless of exceptions.")


