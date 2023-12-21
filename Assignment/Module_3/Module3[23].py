'''
23] Write a Python class named Rectangle constructed by a length and width and a method
          which will compute the area of a rectangle.
'''
class area_rectangle:
    def __init__(self, x, y):
        # Instance attributes 'height' and 'width'
        self.height = x
        self.width = y
    # Instance method 'display' to calculate and print the area of the rectangle
    def display(self):
        # Calculate the area and print the result
        print("Area of rectangle is:", self.height * self.width)
# Get user input for the dimensions of the rectangle
a = int(input("Enter the height (a): "))
b = int(input("Enter the width (b): "))
# Create an instance 'r' of the 'area_rectangle' class with user-provided dimensions
r = area_rectangle(a, b)
# Call the 'display' method to calculate and print the area of the rectangle
r.display()

