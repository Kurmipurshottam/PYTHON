class bird:
    def duck(self):
        self.age=12 #public
        self._sound="quack quack" #protected
        self.__name="x duck" #private
# goose class inherit from bird
class goose(bird):
    def display(self):
        print("Age = ",self.age)#public data access
        print("sound = ",self._sound)#protected access because it is a child of bird class
        print("Name = ",self._bird__name)#private data access using name mangling
# name mangling : it can use for access the private data
#syntax : _classname__privatedata
#creating object of goose class
g=goose()
g.duck()
g.display()
