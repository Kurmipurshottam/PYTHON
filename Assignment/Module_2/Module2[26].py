# 26] Write a Python program to replace last value of tuples in a list.
list1=[(1,2,3),(4,5,6),(7,8,9)]
print(list1)
list2=[]
for item in list1:
#replace last valu of tuple and store in other veriable
    n=item[:-1]+(100,)
#append in to the list2
    list2.append(n)
print(list2)



