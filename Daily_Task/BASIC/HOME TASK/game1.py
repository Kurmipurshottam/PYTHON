import random
lucky_number=random.randint(1 , 100)
print(lucky_number)
print("guess any number between 1 to 100 : :")

status=True
chance=1
while chance<=5 and status:
    print("chance = ",chance)
    no=int(input("enter the number : :"))
    if(no==lucky_number):
        print("congratilation you win")
        status=False
    elif(no>lucky_number):
        print("think lesser number")
    elif(no<lucky_number):
        print("think greater number")
    chance+=1
    if(chance>5):
        con=input("Do you want to continue : :")
        if(con=='yes'):
            chance=1
            status=True
        else:
            status=False
            
            
