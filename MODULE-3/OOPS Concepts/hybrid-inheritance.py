#hybrid inheritance
# a class
class a:
    def show_a(self):
        print("a class")
# b class inherit from a      
class b(a):
    def show_b(self):
        print("b class")
# c class inherit from b
class c(b):
    def show_c(self):
        print("c class")
# d class inherit from b
class d(b):
    def show_d(self):
        print("d class")
#creating object of d class
d1=d()
#calling function using d class object
d1.show_d()
d1.show_b()
#creating object of c class
c1=c()
#calling function using c class object
c1.show_c()
c1.show_b()
#creating object of b class
b1=b()
#calling function using b class object
b1.show_b()
b1.show_a()


        
