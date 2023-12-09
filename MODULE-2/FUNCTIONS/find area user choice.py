def area_finder():
    print("========== Area finder ==========")
    print("1. Area of Circle")
    print("2. Area of Triangle")
    print("3. Area of Rectangle")
    choice=int(input("Enter your choice = "))
    if choice==1:
        radius=float(input("Enter Your Radius = "))
        area=3.14*radius*radius
        print("Area of Circle = ",area)
    elif choice==2:
        height=float(input("Enter Your Height = "))
        base=float(input("Enter Your Base = "))
        area=0.5*height*base
        print("Area of Triangle = ",area)
    elif choice==3:
        length=float(input("Enter Your Length = "))
        width=float(input("Enter Your Width = "))
        area=length*width
        print("Area of Rectangle = ",area)

area_finder()
print(": :Thank You : :")



        
