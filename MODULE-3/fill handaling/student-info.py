f=open('student_info.txt','w')

for i in range(3):
    name=input("Enter name = ")
    i_d=int(input("Enter id = "))
    f.write(f'Name {i+1}= {name} , Id = {i_d}\n')

f.close()


