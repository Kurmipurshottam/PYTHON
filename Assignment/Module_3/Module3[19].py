'''
19] How Do You Handle Exceptions With Try/Except/Finally In Python ? Explain with coding snippets.
 ->  Try: The try block test the code there are some error or not.
 ->  Except: the except block is handel the error.You can have multiple except blocks to handle different
                   types of exceptions.
 ->  Finally: The finally block is always executed even exception occurred or not. 
'''
try:
    # Attempt to get user input and perform a division
    x = int(input("Enter x = "))  
    y = int(input("Enter y = "))  
    result = x / y  # Attempting a division operation
    print("Division result:", result)
except ZeroDivisionError:
    # Handling the specific exception when division by zero occurs
    print("Error: Cannot divide by zero!")
finally:
    # Code to be executed whether an exception occurs or not
    print("Finally block: This will always be executed, regardless of exceptions.")

