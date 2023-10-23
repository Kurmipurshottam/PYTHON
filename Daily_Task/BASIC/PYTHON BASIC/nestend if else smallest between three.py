#smallest between three value
no1=int(input("Enter number one = "))
no2=int(input("Enter number second = "))
no3=int(input("Enter number thired = "))
if no1<no2:
    if no1<no3:
        print("no1 is smallest number")
    else:
        print("no3 is smallest")
else:
    if no2<no3:
        print("no2 is smallest number")
    else:
        print("no3 is smallest number")
   
