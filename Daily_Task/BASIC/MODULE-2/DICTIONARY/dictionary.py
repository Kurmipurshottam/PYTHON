# empty decleration
dict11={}
dict12=dict()
print(dict11)
print(dict12)
#access dictionary
d1={'k1':1,'k2':2,'k3':3}
d2={'k2':67,'k5':90}
#return value hold by key
print(d1['k1'])
#value assignment / or change
d1['k2']=98
#update dictonary
d1.update(d2)
#add new element to dictonary
d1['k4']=70
#copy dictonary
dx={'k1':90,'k2':3}
dx=d2.copy()
print("copy dictonary = ",dx)
print(d1)
