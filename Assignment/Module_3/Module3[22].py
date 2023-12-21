'''
 22] How to Define a Class in Python? What Is Self? Give An Example Of A Python Class.
 -> In Python, a class is a blueprint for creating objects. Objects are instances of a class, and
      each object can have attributes (characteristics) and methods (functions) associated with
      it. The class defines the structure of the objects, encapsulating data and behavior. Here's a
      basic overview of how to define a class in Python:
 -> Class Declaration:-
 -> To define a class, you use the class keyword, followed by the class name.Conventionally, class
      names in Python use CamelCase.
==========================What is self?===============================
 -> In Python, self is a convention and not a reserved keyword. It is used as the first parameter
      in the method definition within a class, representing the instance of the class. The purpose
      of self is to reference the instance of the class and allows youmto access its attributes and methods.
==========================Example of Class===============================
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
'''
