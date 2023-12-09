list=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for i in list:
    if i%2==0:
        even+=i
    else:
        odd+=i
print("sum of even number = ",even)
print("sum of odd number  =",odd) 
