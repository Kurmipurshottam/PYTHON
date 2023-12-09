#multilevel level inheritance
#parent class
class parent:
    def display(self):
        print("parent class")
#child class inherit from parent class
class child(parent):
    def show(self):
        print("child class")
#grend-child class inherit from parent class and child class
class g_child(child):
    def g_show(self):
        print("g_chile class")
#creating object of grend-child class       
c = g_child()
#calling functions
c.show()
c.display()
c.g_show()
