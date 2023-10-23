count=0
odd=0

for i in range(1,11):
    no=int(input("enter number = "))
    if no%2==0:
       count+=1
    else:
        odd+=1
print("count=",count)
print("odd=",odd)
