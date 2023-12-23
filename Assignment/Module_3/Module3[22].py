'''
 22] How to Define a Class in Python? What Is Self? Give An Example Of A Python Class.
 -> A class is a blueprint of the objects and it define the behaviour of the object.
      class is a collection of variables and method
 -> Class Declaration:-
 -> To define a class, you use the class keyword, followed by the class name.
==========================What is self?===============================
 -> In Python, self is not a reserved keyword. It is used as the first parameter
      in the method.
==========================Example of Class===============================
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says Woof!")
# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)
# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name} and it is {my_dog.age} years old.")
my_dog.bark()

