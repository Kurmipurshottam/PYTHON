from tkinter import *
import pymysql
from tkinter import messagebox as msg

mydb = pymysql.connect(host="localhost",user="root",password="",database="college2_data")
mycursor=mydb.cursor()



def insert_fun():
    root = Tk()
    root.geometry('550x330')
    root.resizable(False,False)
    root.title('Insert Operation')
    Title = Label(root,text='Crud Operation',font=('arial',17,'bold'))
    Title.place(x=180,y=10)
    id = Label(root,text='Enter id : ',font=('arial',12,'bold'))
    id.place(x=30,y=70)
    e_id = Entry(root,text='Enter id : ')
    e_id.place(x=330,y=70)
    name = Label(root,text='Enter Name : ',font=('arial',12,'bold'))
    name.place(x=30,y=120)
    e_name = Entry(root,text='Enter Name : ')
    e_name.place(x=330,y=120)
    subject = Label(root,text='Enter Subject Name : ',font=('arial',12,'bold'))
    subject.place(x=30,y=170)
    e_subject = Entry(root,text='Enter subject Name : ')
    e_subject.place(x=330,y=170)

    def insert():
        if e_id.get()=="" or e_name.get()=="" or e_subject.get()=="":
            msg.showinfo("Insert Status","Data Entered Fail")
        else:
            # mycursor=mydb.cursor()
            query="insert into student(id,name,subject) values(%s,%s,%s)"
            args=(e_id.get(),e_name.get(),e_subject.get())
            mycursor.execute(query,args)
            mydb.commit()
            e_id.delete(0,'end')
            e_name.delete(0,'end')
            e_subject.delete(0,'end')
            msg.showinfo("Insert Status","Data Entered successfully")
            root.destroy()

    insert = Button(root,text='insert',font=('arial',14,'bold'),bg='red',command=insert)
    insert.place(x=230,y=250)

def update_fun():
    root = Tk()
    root.geometry('550x330')
    root.resizable(False,False)
    root.title('Update Operation')
    Title = Label(root,text='Crud Operation',font=('arial',17,'bold'))
    Title.place(x=180,y=10)
    id = Label(root,text='Enter id : ',font=('arial',12,'bold'))
    id.place(x=30,y=70)
    e_id = Entry(root,text='Enter id : ')
    e_id.place(x=330,y=70)
    name = Label(root,text='Enter Name : ',font=('arial',12,'bold'))
    name.place(x=30,y=120)
    e_name = Entry(root,text='Enter Name : ')
    e_name.place(x=330,y=120)
    subject = Label(root,text='Enter Subject Name : ',font=('arial',12,'bold'))
    subject.place(x=30,y=170)
    e_subject = Entry(root,text='Enter subject Name : ')
    e_subject.place(x=330,y=170)
    def update():
        if e_id.get()=="":
            msg.showinfo("Update Status","Data Updated Fail")
        else:
            # mycursor=mydb.cursor()
            query="update student set name='%s',subject='%s' where id=%s"
            args=(e_name.get(),e_subject.get(),e_id.get())
            mycursor.execute(query%args)
            mydb.commit()
            e_name.delete(0,'end')
            e_subject.delete(0,'end')
            e_id.delete(0,'end')
            msg.showinfo("Update Status","Data Updated successfully")
            root.destroy()

    update = Button(root,text='update',font=('arial',14,'bold'),bg='red',command=update)
    update.place(x=230,y=250)


def delete_fun():
    root = Tk()
    root.geometry('500x200')
    root.resizable(False,False)
    root.title('Delete Operation')
    Title = Label(root,text='Crud Operation',font=('arial',17,'bold'))
    Title.place(x=180,y=10)
    id = Label(root,text='Enter id : ',font=('arial',12,'bold'))
    id.place(x=70,y=70)
    e_id = Entry(root,text='Enter id : ')
    e_id.place(x=250,y=70)
    def delete():
        if e_id.get()=="":
            msg.showinfo("Delete Status","Data Not Delete Yet")
        else:
            query="delete from student where id=%s"
            args=(e_id.get())
            mycursor.execute(query,args)
            mydb.commit()
            e_id.delete(0,'end')
            msg.showinfo("Delete Status","successfully deleted !!")
            root.destroy()

    delete = Button(root,text='delete',font=('arial',14,'bold'),bg='red',command=delete)
    delete.place(x=200,y=130)


def search_fun():
    root = Tk()
    root.geometry('500x200')
    root.resizable(False,False)
    root.title('Search Operation')
    Title = Label(root,text='Crud Operation',font=('arial',17,'bold'))
    Title.place(x=180,y=10)
    id = Label(root,text='Enter id : ',font=('arial',12,'bold'))
    id.place(x=70,y=70)
    e_id = Entry(root,text='Enter id : ')
    e_id.place(x=250,y=70)
    def search():
        if e_id.get()=="":
            msg.showinfo("Delete Status","Serch Faild")
        else:
            query="select * from student where id=%s "
            args=(e_id.get())
            mycursor.execute(query,args)
            res=mycursor.fetchone()
            print(res)
            mydb.commit()
            e_id.delete(0,'end')
            msg.showinfo("Delete Status","Search successfully !!")
            root.destroy()

    search = Button(root,text='search',font=('arial',14,'bold'),bg='red',command=search)
    search.place(x=200,y=130)


def exit_fun():
    exit() 