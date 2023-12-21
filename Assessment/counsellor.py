students ={} # Create an empty dictionary to store student records
def add_student():
    a = int(input("how many records you want to enter = "))  # Get the number of records to input

    for i in range(a):
        s_no = int(input("enter serial number = "))  # Get serial number for the student
        f_1 = {}  # Create a dictionary to store personal information of the student
        students[s_no] = f_1  # Add personal information dictionary to the students dictionary

        f_name = input("enter first name = ")  # Get first name of the student
        l_name = input("enter last name = ")  # Get last name of the student
        f_1["fname"] = f_name  # Add first name to personal information dictionary
        f_1["lname"] = l_name  # Add last name to personal information dictionary

        c_no = input("enter contact number = ")
        if c_no.isdigit():  # Check if the input is a valid integer for contact number
            f_1["contact"] = c_no  # Add contact number to personal information dictionary
        else:
            print(": : invalid ! : : please enter valid input ?")
            c_no = input("enter contact number = ")
            f_1["contact"] = c_no  # Retry entering contact number and add to personal information dictionary

        f_2 = {}  # Create a dictionary to store subject-wise information of the student
        f_subject = input("enter a subject = ")
        students[s_no]["subject"] = f_2  # Add subject-wise information dictionary to the students dictionary

        f_3 = {}  # Create a dictionary to store marks and fees for the first subject
        f_mark = int(input("enter a mark = "))
        f_fees = int(input("enter a fees = "))
        f_3["mark"] = f_mark  # Add mark to subject-wise information dictionary
        f_3["fees"] = f_fees  # Add fees to subject-wise information dictionary
        f_2[f_subject] = f_3  # Add first subject's information to subject-wise information dictionary

        f_4 = {}  # Create a dictionary to store marks and fees for the second subject
        s_subject = input("enter a subject = ")
        s_mark = int(input("enter a mark = "))
        s_fees = int(input("enter a fees = "))
        f_4["mark"] = s_mark  # Add mark to subject-wise information dictionary
        f_4["fees"] = s_fees  # Add fees to subject-wise information dictionary
        f_2[s_subject] = f_4  # Add second subject's information to subject-wise information dictionary

    print(": : details : :\n", students)  # Print the details of all the students
    try:
        file=open("counsellor.txt","w")
        file.write(str(students))
        file.close()
    except:
        print(": : student added unsuccessfully : :")
    else:
        print(": : student added successfully : :")
add_student()

def remove_student():
    se_n=int(input("enter serial number to remove student = "))
    if se_n in students:
        remove_students=students.pop(se_n)
        print(": : after remove : :\n",students)
    else:
        print(": : student not found : :")
    file=open("counsellor.txt","a")
    file.remove()
    file.write(str(students))
    file.close()
'''    
    def xyz():
        file=open("counsellor.txt","r")
        line=file.readlines()
        file.close()
        file=open("counsellor.txt","w")
        for i in line:
            students=i.strip().split(',')
            c_s_no=students[0]
            if c_s_no==s_no:
                continue
            file.write(line)
        file.close()
        print("File updated successfully.")
    xyz()
    '''
remove_student()

'''
def view_all_students():
    print(": : all students : :")
    print(students)
view_all_students()

def view_specific_students():
    s_en=int(input("enter serial number to find  student = "))
    if s_en in students:
        student_info=students[s_en]
    else:
        print(": : student not found : :")
    print(f' : : {s_en} serial number student : :')
    print(students)
view_specific_students()
'''
