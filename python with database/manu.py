import pymysql
mydb = pymysql.connect(host="localhost",user="root",password="",database="python")
mycursor=mydb.cursor()
menu="""

    press 1 for add student
    press 2 for update student
    press 3 for delete student
    press 4 for search student
    press 5 for search all student
    """
def addoperation():
    name=input("enter name = ")
    subject=input("enter subject = ")
    args=(name,subject)
    query="insert into student (name,subject) values ('%s','%s')"
    mycursor.execute(query % args)
    mydb.commit()
    print("successfully added !!")

def updateoperation():
    id=int(input("which student you want to update enter id = "))
    name=input("enter update name = ")
    subject=input("enter update subject = ")
    query="update student set name='%s',subject='%s'where id=%s"
    args=(name,subject,id)
    mycursor.execute(query % args)
    mydb.commit()
    print("successfully updated !!")

def deleteoperation():
    id=int(input("which student you want to delete enter id = "))
    query="delete from student where id='%s'"
    args=(id)
    mycursor.execute(query % args)
    mydb.commit()
    print("successfully deleted !!")

def searchoperation():
    name=input("enter your name = ")
    query="select * from student where name = '%s' "
    args=(name)
    mycursor.execute(query%args)
    res=mycursor.fetchone()
    print(res[0])
    print(res[1])
    print(res[2])
    mydb.commit()
    print("successfully serched !!")

def searchalloperation():
    query="select * from student "
    mycursor.execute(query)
    res=mycursor.fetchall()
    print(res)
    mydb.commit()
    print("successfully serched !!")

status=True
while status:
    print(menu)
    choice=int(input("enter your choice = "))
    if choice == 1:
        addoperation()
    elif choice == 2:
        updateoperation()
    elif choice == 3:
        deleteoperation()
    elif choice ==4:
        searchoperation()
    elif choice ==5:
        searchalloperation()
    u_choice=input("do you want to perform more operation y for yes and n for no = ")
    if u_choice == 'y':
        status=True
    else:
        status=False
    














