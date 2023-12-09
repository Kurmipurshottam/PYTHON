#single level inheritance
#parent class
class parent:
    def display(self):
        print("parent class")
#child class inherit from parent class
class child(parent):
    def show(self):
        print("child class")
#creating object of child class
c = child()
#calling function
c.show()
c.display()
