def calculater():
    status=True
    while status:
        print("\n==========Choice Board==========")
        print("\t1. Addition")
        print("\t2. Substraction")
        print("\t3. Multiplication")
        print("\t4. Division")
        print("\t5. Modulo")
        print("\t6. Exit")
        print("==============================")
        ch=int(input("Enter Your Choice :- "))
        if ch==1:
            no1=int(input("Enter No1 :- "))
            no2=int(input("Enter No2 :- "))
            print(no1,"+",no2," :- ",no1+no2)
        elif ch==2:
            no1=int(input("Enter No1 :- "))
            no2=int(input("Enter No2 :- "))
            print(no1,"-",no2," :- ",no1-no2)
        elif ch==3:
            no1=int(input("Enter No1 :- "))
            no2=int(input("Enter No2 :- "))
            print(no1,"*",no2," :- ",no1*no2)
        elif ch==4:
            no1=int(input("Enter No1 :- "))
            no2=int(input("Enter No2 :- "))
            print(no1,"/",no2," :- ",no1/no2)
        elif ch==5:
            no1=int(input("Enter No1 :- "))
            no2=int(input("Enter No2 :- "))
            print(no1,"%",no2," :- ",no1%no2)
        else:
            exit()
        print("For Continue Enter :- yes")
        print("For Continue Enter :- no")
        print("For Exit Enter Anything")
        choice=input("Do You Want To Continue :- ")
        if choice=='yes':
            status=True
        elif choice=='no':
            status=False
        else:
            print("Enter Valid Input")
            exit()
            
calculater()
