#.keys() : it return only key from dictionary
#.values() : it returns only value from dictionary
#.items() : return pair of key and value
d1={'name':'nikhil','age':19,'gender':'male'}
print(d1)
for i in d1:#it returns only keys
    print("dictionary",i)
for i in d1.keys():#it is also return keys
    print("keys",i)
for i in d1.values():# it is return values only
    print("values : ",i)
for i in d1.items():# it is return pair of element means key:values
    print("pair of values : ",i)
#.clear() : remove all elements
#.copy() : copy dictionary to other
#.update() : will updaate existing dictionary with new
d2=d1.copy()
d1.clear()
print("copy method = ",d2)
print("cleare method = ",d1)
d3.update(d2)
print("update method = ",d3)
del d3['gender']
print("delete",d3)
