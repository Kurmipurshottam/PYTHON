#multipel level inheritance
#first parent class
class parent:
    def display(self):
        print("parent class")
#second parent class
class parent2:
    def show(self):
        print("parent2 class")
#child class inharit from first and second parent class
class child(parent,parent2):
    def c_show(self):
        print("chile class")
#creating object of child class 
c = child()
#calling functions
c.c_show()
c.display()
c.show()
