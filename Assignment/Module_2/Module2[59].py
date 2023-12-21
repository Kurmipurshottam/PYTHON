# 59]  Write a Python program to convert degree to radian.
# Function to convert degrees to radians
def degrees(degree):
    radians = degree * (3.14/ 180)  # Formula to convert degrees to radians
    return radians
# Input degrees
degree=float(input("Entre degree to convert radian = "))
# Convert degrees to radians
radians = degrees(degree)
# Display the result
print(f"{degree} degrees is equal to {radians} radians.")
