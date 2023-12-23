# 16] Can one block of except statements handle multiple exception ?
try:
    no1 = int(input("Enter a number: "))
    no2 = int(input("Enter a number: "))
    result = no1 / no2  # Attempting a division operation
except (ValueError):
    # Handling the exceptions when the input cannot be converted to an integer
    print("Invalid input.")
except ZeroDivisionError:
    # Handling the specific exception when division by zero occurs
    print("Cannot divide by zero!")
else:
    # Code to be executed if no exception is raised in the try block
    print("Division successful. Result:", result)


