mark1=int(input("Enter your python marks = "))
mark2=int(input("Enter your java marks = "))
mark3=int(input("Enter your php marks = "))
if mark1>100 or mark2>100 or mark3>100:
    print("Enter valid marks")
elif mark1<35 or mark2<35 or mark3<35:
    print("Fail")
else:
    total=mark1+mark2+mark3
    print("total mark is = ",total)
    per=total/3
    print("percentage = ",per)
    if per>=90:
        print("Grad is A+")
    elif per>=75 and per<90:
        print("Grad is A")
    elif per>=60 and per<75:
        print("Grad is B")
    elif per>=50 and per<60:
        print("Grad is C")
    elif per>=35 and per<50:
        print("Grad is D")
    elif per>=0 and per<35:
        print("Fail")
    else:
        print("Invalid Input")
