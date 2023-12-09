# 62]  Write a Python program to calculate surface volume and area of a cylinde
# Function to calculate the surface area of a cylinder
def cylinder_surface_area(radius, height):
    area = 2 * 3.14 * radius**2 + 2 * 3.14* radius * height
    return area
# Function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    volume = 3.14 * radius**2 * height
    return volume
# Get user input for the radius and height of the cylinder
radius = float(input("Enter the radius of the cylinder = "))
height = float(input("Enter the height of the cylinder = "))
# Calculate the surface area and volume using the functions
surface_area = cylinder_surface_area(radius, height)
volume = cylinder_volume(radius, height)
# Print the results
print(f"The surface area of the cylinder is = {surface_area}")
print(f"The volume of the cylinder is = {volume}")
