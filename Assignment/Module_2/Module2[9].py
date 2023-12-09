'''
9] Write a Python function that takes two lists and returns true if they have
at least one common member.
'''
#creating function
def match_data(a,b):
    for i in list1:
        for j in list2:
             if i==j:
                result=True
                return result
             else:
                result=False
                return result
list1=[]
list2=[]
#input for first list
n=int(input("how many element do you want to enter in list1 = "))
for i in range(n):
    a=int(input("enter value = "))
    list1.append(a)
print("list1 = ",list1)
#input for second list
m=int(input("how many element do you want to enter in list2 = "))
for i in range(m):
    b=int(input("enter value = "))
    list2.append(b)
print("list2 = ",list2)
#function calling
print("data match = ",match_data(list1,list2))
