'''
19] How Do You Handle Exceptions With Try/Except/Finally In Python ? Explain with coding snippets.
 ->  Handling exceptions in Python using try, except, and finally blocks allows you to gracefully
       manage errors and ensure that necessary cleanup operations are performed. Here are coding
       snippets to illustrate how to use try, except, and finally:
'''
try:
    # Attempt to get user input and perform a division
    x = int(input("Enter a number: "))  # Try to convert user input to an integer
    result = 10 / x  # Attempting a division operation
    print("Division result:", result)
except ZeroDivisionError:
    # Handling the specific exception when division by zero occurs
    print("Error: Cannot divide by zero!")
finally:
    # Code to be executed whether an exception occurs or not
    print("Finally block: This will always be executed, regardless of exceptions.")

