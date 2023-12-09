print("<<<<<<<<<Args>>>>>>>>>>")
#args : arguments  
def fun1(*x):
    for i in x:
        print(i)
list1=[1,2,3,4,5,6]
x=23
k1=90
a=12
fun1(list1,x,k1,a)
print("<<<<<<<<<<Kwargs>>>>>>>>>>>")
#Kwargs : keyword argument
def fun2(**x):
    for i,k in x.items():
        print(f'{i} = {k}')
fun2(x=23,k=67 , list2=[1,2,3],k2=90)
