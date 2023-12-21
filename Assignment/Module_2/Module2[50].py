# 50]  Write a Python function to check whether a number is perfect or not.
def perfect_num(num):
    sum = 0
    # Iterate through numbers from 1 to (num - 1) to find divisors of num
    for i in range(1, num):
        # Check if i is a divisor of num
        if num % i == 0:
            sum += i  # Add divisor to sum
    # Check if the sum of divisors equals the original number
    if sum == num:
        print("The number is perfect")
    else:
        print("The number is not perfect")
# Take user input for the number
num = int(input("Enter number: "))
# Call the perfect_num function with the user-input number as an argument
perfect_num(num)
