dict={'abc':10,'def':5,'xyz':20}
temp = None
#answer
#dict1={'def':5,'abc':10,'xyz':20}

s1 = dict.values()
s2 = list(s1)

for i in s2:
    for j in range(i+1):
        if i>j:
            temp = i
            i = j
            j = temp


print(s2)






