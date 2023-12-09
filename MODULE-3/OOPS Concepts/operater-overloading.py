#operater overloading
class Demo:
    def __init__(self,x):
        self.n=x
# it use for perform operation between two object
    def subtraction(self,y):
        return self.n-y.n
d=Demo(43)
d1=Demo(23)
print(d.subtraction(d1))
