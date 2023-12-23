'''
26] Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
 ->  Inheritance is a fundamental concept in object-oriented programming . one class deived from other
       class is called inheritance. it is allow code reuseability.
=============================================================================
 -> In Python, __init__ is a special method and also know as an "constructor. "It is automatically
      called when an object is created from a class.
=============================================================================
 -> In Python, a constructor is a special method called __init__ that is automatically executed when
      an object is created from a class.
=============================================================================
 -> Constructor means two or more function name is same but defferent perameter.
'''
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
# Creating instances of the child classes
dog_instance = Dog("rockey")
cat_instance = Cat("kity")
# Calling the speak method of each instance
print(dog_instance.speak())
print(cat_instance.speak()) 
