import pymysql
mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists tops_python")
mydb = pymysql.connect(host="localhost",user="root",password="",database="tops_python")
mycursor=mydb.cursor()
mycursor.execute("create table if not exists student(id int primary key auto_increment,name varchar(20),subject varchar(20))")
mydb.commit()