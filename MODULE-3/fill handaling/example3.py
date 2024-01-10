f=open("example3.txt","a")
for i in range(1,6):
    name=input("Enter name : ")
    f.write("\n"+name)
f.close()