#heriachical level inheritance
#parent class
class parent:
    def display(self):
        print("parent class")
#first child class inherit from parent class
class child(parent):
    def show(self):
        print("child class")
#second child class inherit from parent class
class child2(parent):
    def c_show(self):
        print("chile2 class")
#creating object of second child      
c = child2()
#calling function using second child object
c.c_show()
c.display()
#creating object of first child
c1=child()
#calling function using first child object
c1.show()
c1.display()
