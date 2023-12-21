# 16] Can one block of except statements handle multiple exception ?
try:
    # Attempt to get user input and perform a division
    user_input = int(input("Enter a number: "))  # Try to convert user input to an integer
    result = 10 / user_input  # Attempting a division operation
except (ValueError, TypeError):
    # Handling the exceptions when the input cannot be converted to an integer
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    # Handling the specific exception when division by zero occurs
    print("Cannot divide by zero!")
else:
    # Code to be executed if no exception is raised in the try block
    print("Division successful. Result:", result)


