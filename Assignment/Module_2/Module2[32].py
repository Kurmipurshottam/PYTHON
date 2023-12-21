# 32] Write a Python script to sort (ascending and descending) a dictionary by value.
dict1={'raj' : 75,'purshottam' : 7,'nikhil' : 111,'smit' : 21}
sort_dict1=sorted(dict1.values())
print(sort_dict1)
d2={}
for i in dict1:
    d2[i][j]=dict1[i][j]
print(dict2)
'''
desc_dict1=sorted(dict1.items()),reversed=True
print(desc_dict1)
'''
