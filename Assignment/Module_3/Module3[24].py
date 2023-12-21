'''
24] Write a Python class named Circle constructed by a radius and two methods which will
       compute the area and the perimeter of a circle.
'''
class circle:
    # Constructor (initializer) method with 'radius' as a parameter
    def __init__(self, radius):
        # Instance attribute 'radius'
        self.radius = radius
    # Method to compute the area of the circle
    def circle_area(self):
        area = 3.14 * self.radius *self.radius
        return area
    # Method to compute the perimeter (circumference) of the circle
    def circle_perimeter(self):
        perimeter = 2 *3.14 * self.radius
        return perimeter
# Get user input for the radius of the circle
radius = float(input("Enter the radius of the circle: "))
# Create an instance 'my_circle' of the 'Circle' class with the user-provided radius
c = circle(radius)
# Calculate and print the area of the circle
area = c.circle_area()
print("Area of the circle = ",area)
# Calculate and print the perimeter of the circle
perimeter = c.circle_perimeter()
print("Perimeter of the circle = ",perimeter)
