# 53] How can you pick a random item from a list or tuple?
# Import the random module to generate random numbers
import random
# Create a list and a tuple
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 4, 9, 16, 25)
# Print the original list and tuple
print("list = ", list1)
print("tuple = ", tuple1)
# Generate and print a random number from the list using random.choice()
random_number_from_list = random.choice(list1)
print("random number from list = ", random_number_from_list)
# Generate and print a random number from the tuple using random.choice()
random_number_from_tuple = random.choice(tuple1)
print("random number from tuple = ", random_number_from_tuple)

