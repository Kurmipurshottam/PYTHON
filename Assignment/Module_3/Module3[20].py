# 20] Write python program that user to enter only odd numbers, else will raise an exception.
while True:
    try:
        # Get user input as an integer
        user_input = int(input("Enter an odd number: "))   
        # Check if the entered number is odd
        if user_input % 2 != 1:
            print("You must enter an odd number.")
        else:
            print(f"You entered an odd number = {user_input}")
            break  # Break out of the loop if a valid odd number is entered   
    except ValueError :
        # Handle the ValueError (non-integer input)
        print("Please enter only odd numbers.")    
    finally:
        # This block is always executed, regardless of whether an exception occurred or not
        print("Program execution complete.")


