from tkinter import *
root = Tk()

#====================Set up the main window====================
root.geometry('1330x770')
root.title("HOTEL MANAGEMENT SYSTEM")
root.resizable(False,False)

#====================Create a label for the title====================
Title = Label(root,text="WELCOME",font=('Copperplate',25,'bold'))
Title.place(x=550,y=10)

#====================Create CHECK IN button====================
c_in=Button(root,text="CHECK IN",font=('Copperplate',25,'bold'),bg='#d9d9d9')
c_in.place(x=100,y=100,height=100,width=500)

#====================Create SHOW GUEST LIST button====================
s_g_list=Button(root,text="SHOW GUEST LIST",font=('Copperplate',25,'bold'),bg='#d9d9d9')
s_g_list.place(x=100,y=230,height=100,width=500)

#====================Create CHECK OUT button====================
c_out=Button(root,text="CHECK OUT",font=('Copperplate',25,'bold'),bg='#d9d9d9')
c_out.place(x=100,y=360,height=100,width=500)

#====================Create GET INFO ANY GUESTT button====================
get_guest=Button(root,text="GET INFO ANY GUEST",font=('Copperplate',25,'bold'),bg='#d9d9d9')
get_guest.place(x=100,y=490,height=100,width=500)

#====================Create EXIT button====================
exit=Button(root,text="EXIT",font=('Copperplate',25,'bold'),bg='#d9d9d9')
exit.place(x=100,y=620,height=100,width=500)

#====================Additional labels for decoration====================
f_text = Label(root,text="HOTEL MANAGEMENT",font=('Copperplate',45,'bold'))
f_text.place(x=630,y=120)

s_text = Label(root,text="PYTHON TKINTER",font=('Copperplate',45,'bold'))
s_text.place(x=700,y=240)

t_text = Label(root,text="GUI",font=('Copperplate',120,'bold'))
t_text.place(x=800,y=340)

#====================Start the main event loop====================
root.mainloop()
