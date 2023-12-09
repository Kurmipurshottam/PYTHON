# 60]  Write a Python program to calculate the area of a trapezoid
# Function to calculate the area of a trapezoid
def trapezoid_area(base1, base2, height):
    area = (base1 + base2) * height / 2
    return area
# Get user input for the lengths of the bases and the height
base1 = float(input("Enter the length of the first base = "))
base2 = float(input("Enter the length of the second base = "))
height = float(input("Enter the height = "))
# Calculate the area using the trapezoid_area function
area_of_trapezoid = trapezoid_area(base1, base2, height)
# Print the result
print(f"The area of the trapezoid is = {area_of_trapezoid}")
