from tkinter import *
import crud_opration as e


root = Tk()
root.geometry('550x150')
root.resizable(False,False)
root.title('Crud Operation')

Title = Label(root,text='Crud Operation',font=('arial',17,'bold'))
Title.place(x=180,y=10)
insert = Button(root,text='insert',font=('arial',14,'bold'),bg='red',command=e.insert_fun)
insert.place(x=40,y=80)
update = Button(root,text='update',font=('arial',14,'bold'),bg='red',command=e.update_fun)
update.place(x=140,y=80)
delete = Button(root,text='delete',font=('arial',14,'bold'),bg='red',command=e.delete_fun)
delete.place(x=250,y=80)
search = Button(root,text='search',font=('arial',14,'bold'),bg='red',command=e.search_fun)
search.place(x=350,y=80)
exit = Button(root,text='exit',font=('arial',14,'bold'),bg='red',command=e.exit_fun)
exit.place(x=460,y=80)

root.mainloop()