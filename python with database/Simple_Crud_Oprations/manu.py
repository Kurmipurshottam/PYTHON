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
    try:
        id = int(input("Enter ID to update: "))
        # Check if the ID exists in the database
        query = "SELECT * FROM student WHERE id = %s"
        mycursor.execute(query%id)
        data = mycursor.fetchone()
        if not data:
            print("No student found with the given ID. Please try again.")
            return

        name=input("enter update name = ")
        subject=input("enter update subject = ")
        query="update student set name='%s',subject='%s'where id=%s"
        args=(name,subject,id)
        mycursor.execute(query % args)
        mydb.commit()
        print("Successfully updated!")
    except:
        print("Invalid input. Please enter a valid ID.")

def deleteoperation():
    try:
        id=int(input("which student you want to delete enter id = "))
        query = "SELECT * FROM student WHERE id = %s"
        args=(id)
        mycursor.execute(query%args)
        data=mycursor.fetchone()
        if not data:
                print("No student found with the given ID. Please try again.")
                return
        query="delete from student where id='%s'"
        args=(id)
        mycursor.execute(query % args)
        mydb.commit()
        print("successfully deleted !!")
    except:
        print("Invalid input. Please enter a valid ID.")


def searchoperation():
    name=input("enter your name = ")
    query="select * from student where name = '%s' "
    args=(name)
    mycursor.execute(query%args)
    res=mycursor.fetchone()
    if res:
        print(f"ID: {res[0]}, Name: {res[1]}, City: {res[2]}")
    else:
        print("No student found with the given ID.")
    mydb.commit()
    print("successfully serched !!")


def searchalloperation():
    query="select * from student "
    mycursor.execute(query)
    res=mycursor.fetchall()
    for row in res:
        print(f"ID: {row[0]}, Name: {row[1]}, City: {row[2]}")
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
    














