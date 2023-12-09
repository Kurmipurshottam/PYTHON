# 61]  Write a Python program to calculate the area of a parallelogram.
# Function to calculate the area of a parallelogram
def parallelogram_area(base, height):
    area = base * height
    return area
# Get user input for the base and height
base = float(input("Enter the length of the base = "))
height = float(input("Enter the height = "))
# Calculate the area using the parallelogram_area function
area_of_parallelogram = parallelogram_area(base, height)
# Print the result
print(f"The area of the parallelogram is = {area_of_parallelogram}")
