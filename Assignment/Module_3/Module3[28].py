'''
28] What is used to check whether an object o is an instance of class A ?
 ->  In Python we have use the isinstance() function to check object is an instance of a particular class.
'''
class A:
    pass
# Creating an instance of class A
obj = A()
# Checking if obj is an instance of class A
if isinstance(obj, A):
    print(": : obj is an instance of class A : :")
else:
    print(": : obj is not an instance of class A : :")
