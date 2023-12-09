# map() : apply function to each element of collect
# syntax : map(fun.iterable)
def xyz(x):
    return x*x
list1=[1,2,3,4,5,6]
print(list(map(xyz,list1)))
