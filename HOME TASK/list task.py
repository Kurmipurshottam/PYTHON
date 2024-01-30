list1=[2,4,6,8]
list2=[12,14,16,18]
# we want output like this = {2: 12, 4: 14, 6: 16, 8: 18}
dic={}
# dic=dict(zip(list1,list2))
# print("dictionary = ",dic)
x=len(list1)
y=len(list2)
for i in range(x):
    for j in range (y):
        if i==j:
            dic[list1[i]]=list2[j]
print("dictionary = ",dic) 