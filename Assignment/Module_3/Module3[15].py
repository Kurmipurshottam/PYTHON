'''
15] When will the else part of try-except-else be executed ?
 ->  The code inside the try block is executed. If an exception occurs during the execution
       of the try block, the corresponding except block is executed to handle the exception.
       If no exception occurs, the else block is executed.
'''
#example :-
try:
    # Code that may raise an exception
    result = 10 / 2  # Attempting a division operation
except ZeroDivisionError:
    # Handling the specific exception when division by zero occurs
    print("Cannot divide by zero!")
else:
    # Code to be executed if no exception is raised in the try block
    print("Division successful. Result =", result)

