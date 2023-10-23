li=[]
a=int(input("how many elemet you want to enter  = "))
for i in range(a):
    no=int(input("enter the element = "))
    li.append(no)
print("before sorting list = ",li)
for i in range(len(li)) :
    for j in range(i+1,len(li)):
        if li[i]<li[j]:
            temp=li[i]
            li[i]=li[j]
            li[j]=temp
print("after sorting list = ",li)
    
