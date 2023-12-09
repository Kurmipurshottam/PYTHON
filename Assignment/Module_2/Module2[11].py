'''
11] Write a Python function that takes a list and returns a new list with unique
elements of the first list.
'''
#creating function
def unique(x):
    a=[]
    for i in x:
        if i not in a:
            a.append(i)
    print("unique list = ",a)
list1=[1,2,3,4,5,6,5,2,4]
print("list = ",list1)
#calling function
unique(list1)

