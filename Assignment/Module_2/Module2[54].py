# 54] How can you pick a random item from a range?
# Import the random module to generate random numbers from a range
import random
# Take user input for the upper range limit
u_range = int(input("Enter the range to get a number = "))
# Generate a random number within the specified range
random_number = random.randint(0, u_range)
# Print the random number
print("Random number from the range is =", random_number)
