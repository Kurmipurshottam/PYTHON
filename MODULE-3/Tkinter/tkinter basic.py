from tkinter import Tk,Label,Entry,Button
#Tk : class from tkinter module
#object creation off tk class
obj = Tk()
obj.title("arithmetic window")
obj.geometry('600x600')
obj.resizable(False,False)
def get_data1():
    data1=e_num1.get()
    data2=e_num2.get()
    print("num 1 = ",data1)
    print("num 2 = ",data2)
    print("num 1 + num 2 = ",int(data1)+int(data2))
def get_data2():
    data1=e_num1.get()
    data2=e_num2.get()
    print("num 1 = ",data1)
    print("num 2 = ",data2)
    print("num 1 - num 2 = ",int(data1)-int(data2))
def get_data3():
    data1=e_num1.get()
    data2=e_num2.get()
    print("num 1 = ",data1)
    print("num 2 = ",data2)
    print("num 1 + num 2 = ",int(data1)/int(data2))
# to write any text on window use label class
heading=Label(obj,text="welcome to window",bg="aqua",fg="black",font="Arial 20 bold")
heading.place(x=150,y=40)
#to close the tkinter window
#obj.mainloop()
#Label
num1=Label(obj, text="enter number1 = ",font=("Arial 15"))
num1.place(x=100,y=90)
num2=Label(obj, text="enter number2 = ",font=("Arial 15"))
num2.place(x=100,y=130)
#entry
e_num1=Entry(obj)
e_num1.place(x=270,y=95)
e_num2=Entry(obj)
e_num2.place(x=270,y=135)
#button
add=Button(obj,text="Addition",command=get_data1)
add.place(x=120,y=180)
sub=Button(obj,text="Substraction",command=get_data2)
sub.place(x=190,y=180)
div=Button(obj,text="Division",command=get_data3)
div.place(x=280,y=179)

