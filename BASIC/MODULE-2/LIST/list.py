li=[2,3,4,5]
li2=[6,7,8,9]
li3=[90,80,70]
li4=[60,50,40]
li.append(20)#add element last position
print("append li in 20  = ",li)
li.append(li2)
print("append li2 in to li = ",li)
li3.insert(2,2.5)#(position,element)specific position on add element
print("insert 2.2 in 2nd position = ",li3)
li4.extend(li)#extend list in the list as element in list4
print("li extend in li4 = ",li4)
li.append(li2)#add list on last position
print(li)
li3.insert(2,[li2])#(position,element)specific position on add list
print(li3)

