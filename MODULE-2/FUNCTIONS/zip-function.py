#zip function
list1=[1,2,3,4]
list2=[4,3,2]
list3=[9,8,7,6]
#zip in form of list
print(list(zip(list1,list2,list3)))
#zip in sequence
for i , j , k in zip(list1,list2,list3):
    print(i)
    print(j)
    print(k)
