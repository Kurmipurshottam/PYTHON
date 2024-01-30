# Importing classes for different roles
import counsellor
import student
import faculty

# Main loop for the Student Management System
while True:
    # Displaying the main menu
    print(": : : : : : : : : : : : : : : : : : : : : : : : Student Management System Menu : : : : : : : : : : : : : : : : : : : : : : : :")
    print("\t\tpress 1 for Counsellor")
    print("\t\tpress 2 for Faculty")
    print("\t\tpress 3 for Student")
    print("\t\tpress 4 for exit")
    print(": : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :")
    # Taking user input for role
    role = int(input("Enter your role = "))

    # Handling different roles
    if role == 1:  # Counsellor
        status = True
        while status:
            counsellor.display()
            choice = int(input("Enter your choice = "))
            if choice == 1:
                counsellor.add_student()
            elif choice == 2:
                counsellor.remove_student()
            elif choice == 3:
                counsellor.view_all_students()
            elif choice == 4:
                counsellor.view_specific_students()
            elif choice == 5:
                status = False
            else:
                print(": : : : : : : Enter valid input : : : : : : :")
                status = True

    elif role == 2:  # Faculty
        f_status = True
        while f_status:
            faculty.display()
            choice = int(input("Enter your choice = "))
            if choice == 1:
                faculty.add_mark_to_student()
            elif choice == 2:
                faculty.view_all_student()
            elif choice == 3:
                f_status = False
            else:
                print(": : : : : : : Enter valid input : : : : : : :")
                f_status = True

    elif role == 3:  # Student
        s_status = True
        while s_status:
            student.display()
            choice = int(input("Enter your choice = "))
            if choice == 1:
                student.view_our_result()
            elif choice == 2:
                s_status = False
            else:
                print(": : : : : : : Enter valid input : : : : : : :")
                s_status = True
    else:
        # Exiting the main loop if the user chooses to exit
        exit()
        # counsellor.exit_function()

                     
              
       

              
            
