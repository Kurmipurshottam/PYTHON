# 6] Write python program that swap two number with temp variable and without temp variable.
print(" : : swap with temp variable so enter = 1 : : ")
print(" : : swap without temp variable so enter = 2 : : ")
ch=int(input("Enter your choice = "))
if ch==1:
    no1=int(input("Enter no1 = "))
    no2=int(input("Enter no2 = "))
    print(" : : before swaping : : ")
    print("Enter no1 = ",no1)
    print("Enter no2 = ",no2)
    print(" : : after swap with temp variable : : ")
    temp=no1
    no1=no2
    no2=temp
    print("Enter no1 = ",no1)
    print("Enter no2 = ",no2)
else:
    no1=int(input("Enter no1 = "))
    no2=int(input("Enter no2 = "))
    print(" : : before swaping : : ")
    print("Enter no1 = ",no1)
    print("Enter no2 = ",no2)
    print(" : : after swap without temp variable : : ")
    no1, no2 = no2, no1
    print("Enter no1 = ",no1)
    print("Enter no2 = ",no2)
