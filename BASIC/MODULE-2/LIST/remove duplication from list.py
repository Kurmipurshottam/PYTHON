li=[12,34,45,56,67,78,89,12,34]
li1=[]
for i in li:
        if i not in li1:
            li1.append(i)
print("list = ",li1)
