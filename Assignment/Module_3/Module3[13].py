'''
13] Explain Exception handling? What is an Error in Python?
 -> Exception handling in Python is a mechanism that allows a program to deal with errors 
      or exceptional situations gracefully rather than abruptly terminating. 
      Errors in Python are represented as exceptions. When an error occurs during the execution
      of a program an exception is raised, and the program flow is interrupted.
 ->  Here are the key components of exception handling in Python:
      Try: The try block encloses the section of code where an exception might occur. 
              It's the segment of code that you want to monitor for errors.
      Except: The except block follows the try block and specifies the code that should be executed
                   if a specific exception occurs.You can have multiple except blocks to handle different
                   types of exceptions.
      Else: The else block contains code that is executed if the try block does not raise an exception.
               It's optional.
      Finally: The finally block contains code that is always executed, whether an exception occurred or not. 
                   It's optional but commonly used for cleanup operations.
==============================What is an Error in Python?====================================
 ->  An "error" in Python generally refers to a situation where the program cannot proceed as intended due to unexpected conditions.
       Errors can be broadly categorized into two types:
 ->  Syntax Errors: These are errors that occur when the Python interpreter encounters invalid Python code. 
       They are detected during the parsing of the code and prevent the program from running.
 ->  Example:
       print("Hello, world!")
 ->  Runtime Errors (Exceptions): These errors occur during the execution of the program. 
       They are not detected by the interpreter until the program is run.

'''




