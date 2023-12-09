# 63] Write a Python program to returns sum of all divisors of a number.
# Input value
number=int(input("enter number = "))
sum = 0  # Initialize the sum
# Iterate from 1 to the number
for i in range(1, number + 1):
    if number % i == 0:  # Check if 'i' is a divisor of 'number'
        sum += i  # Add 'i' to the sum 
# Display the result
print(f"The sum of divisors of {number} is = {sum}")
