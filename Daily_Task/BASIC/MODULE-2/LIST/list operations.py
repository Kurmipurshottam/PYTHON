l_even=[]
l_odd=[]
for i in range(10):
    num=int(input("enter the number = "))
    if num%2==0:
        l_even.append(num)
    else:
        l_odd.append(num)
print("even list =",l_even)
print("odd list =",l_odd)
'''
for insert in list : : :
append(): use to add element at the last of list
insert(): use to add element in specific position in list
extend(): use to add whole list as an element in list
'''
'''
for delete element in list : : :
.pop() : use with two types
    without index : will remove last element in list
    with index : will remove specific element by position in list
.remove() : will remove element by itself
del{keeyword} : remove specific indexed element
.clear() : will remove all element from list
'''
