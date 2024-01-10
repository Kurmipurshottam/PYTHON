def display():
    # Displaying options for the user
    print("\t\t1. Add student")
    print("\t\t2. Remove student")
    print("\t\t3. View all student")
    print("\t\t4. View specific student")
    print("\t\t5. Back to Main Menu")

# Create an empty dictionary to store student records
students = {}

#=========================add students function==============================

def add_student():
    try:
        # Get the number of records to input
        a = int(input("How many records do you want to enter? "))

        # Iterate through the specified number of records
        for i in range(a):
            # Get serial number for the student
            s_no = int(input("Enter serial number: "))

            # Create a dictionary to store personal information of the student
            f_1 = {}
            students[s_no] = f_1  # Add personal information dictionary to the students dictionary

            # Get first name and last name of the student
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            f_1["fname"] = f_name  # Add first name to personal information dictionary
            f_1["lname"] = l_name  # Add last name to personal information dictionary

            # Get and validate contact number
            c_no = input("Enter contact number: ")
            while not c_no.isdigit():
                print(": : Invalid input! : : Please enter a valid integer for contact number.")
                c_no = input("Enter contact number: ")
            f_1["contact"] = c_no  # Add contact number to personal information dictionary

            # Create a dictionary to store subject-wise information of the student
            f_2 = {}
            f_subject = input("Enter a subject: ")
            students[s_no]["subject"] = f_2  # Add subject-wise information dictionary to the students dictionary

            # Create a dictionary to store marks and fees for the first subject
            f_3 = {}
            f_mark = int(input("Enter a mark: "))
            f_fees = int(input("Enter a fee: "))
            f_3["mark"] = f_mark  # Add mark to subject-wise information dictionary
            f_3["fees"] = f_fees  # Add fee to subject-wise information dictionary
            f_2[f_subject] = f_3  # Add first subject's information to subject-wise information dictionary

            # Create a dictionary to store marks and fees for the second subject
            f_4 = {}
            s_subject = input("Enter a subject: ")
            s_mark = int(input("Enter a mark: "))
            s_fees = int(input("Enter a fee: "))
            f_4["mark"] = s_mark  # Add mark to subject-wise information dictionary
            f_4["fees"] = s_fees  # Add fee to subject-wise information dictionary
            f_2[s_subject] = f_4  # Add second subject's information to subject-wise information dictionary

        # Open the file in write mode to update the content
        file = open("counsellor.txt", "w")
        # Write the updated content to the file
        file.write(str(students))
        # Close the file after writing
        file.close()

        # Display success message
        print(": : Student added successfully : :")

    except FileNotFoundError:
        # Handling the case where the file is not found
        print(": : Student addition unsuccessful - File Not Found : :")

#============================remove students function===========================
        
def remove_student():
    try:
        # Opening the file in read mode
        file = open("counsellor.txt", "r")

        # Reading the first line of the file
        data = file.readline()

        # Converting the content to a dictionary using eval
        content = eval(data)

        # Displaying the current content (for debugging purposes)
        print("Current content:", content)

        # Closing the file after reading
        file.close()

        # Taking input for the serial number to remove a student
        s_no = int(input("Enter serial number to remove student: "))

        # Iterating through items in the content dictionary
        for item in content.items():
            # Checking if the input serial number is present in the current item
            if s_no in item:
                # Removing the student with the specified serial number
                content_delete = content.pop(s_no)
                break

        # Opening the file in write mode to update the content
        file = open("counsellor.txt", "w")
        # Writing the updated content to the file
        file.write(str(content))
        # Closing the file after writing
        file.close()

        # Displaying success message
        print(": : Student removed successfully : :")

    except FileNotFoundError:
        # Handling the case where the file is not found
        print(": : Student removal unsuccessful - File Not Found : :")

#=======================view all students functions===========================
        
def view_all_students():
    try:
        # Try to open the file "counsellor.txt" in read mode
        file = open("counsellor.txt", "r")
        # Read all lines from the file and store them in f_data
        f_data = file.readline()
        # Print a message indicating that all students are being displayed
        print(": : all students : :")
        # Print the data read from the file (all students)
        print(f_data)
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(": : view student unsuccessfully : :")
    else:
        # Close the file and print a success message if the file is found
        file.close()
        print(": : view student successfully : :")
        
#=============================view specific students function=========================
        
def view_specific_students():
    try:
        # Opening the file in read mode
        file = open("counsellor.txt", "r")

        # Reading the first line of the file
        data = file.readline()

        # Converting the content to a dictionary using eval
        content = eval(data)

        # Taking input for the serial number to view a specific student
        s_no = int(input("Enter serial number to view specific student: "))

        # Initializing an empty dictionary for the specific student
        specific_student = {}

        # Iterating through items in the content dictionary
        for item in content.items():
            # Checking if the input serial number is present in the current item
            if s_no in item:
                specific_student = item
                break

        # Checking if a specific student was found
        if specific_student:
            print("Specific student details:", specific_student)
        else:
            print(": : Student not found : :")

    except FileNotFoundError:
        # Handling the case where the file is not found
        print("File Not Found")




