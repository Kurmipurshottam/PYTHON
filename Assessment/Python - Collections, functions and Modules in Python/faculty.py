import counsellor

# Function to display options for the faculty
def display():
    print("\t\t1. Add Mark to Student")
    print("\t\t2. View all student")
    print("\t\t3. Back to Main Menu")
    
#=========================add mark to students function==============================
    
def add_mark_to_student():
    try:
        # Read the file
        with open("counsellor.txt", "r") as file:
            students = eval(file.read())

        # Get user input for updating marks
        student_id = int(input("Enter student ID to update marks: "))
        subject = input("Enter subject to update marks: ")
        new_mark = int(input("Enter new mark: "))

        # Update marks
        if student_id in students and subject in students[student_id]['subject']:
            students[student_id]['subject'][subject]['mark'] = new_mark
            print("Marks updated successfully.")
        else:
            print(f"Student ID {student_id} or subject {subject} not found.")

        # Display the updated data
        print("\nUpdated Data:")
        print(students)

        # Write the updated data back to the file
        with open("counsellor.txt", "w") as file:
            file.write(str(students))

    except FileNotFoundError:
        # Handle the case where the file is not found
        print(": : Marks update unsuccessful - File Not Found : :")
        
#=========================view all students function==============================

def view_all_student():
    try:
        # Try to open the file "counsellor.txt" in read mode
        file = open("counsellor.txt", "r")
        
        # Read all lines from the file and store them in f_data
        f_data = file.readline()
        
        # Print a message indicating that all students are being displayed
        print(": : All students : :")
        
        # Print the data read from the file (all students)
        print(f_data)

    except FileNotFoundError:
        # Handle the case where the file is not found
        print(": : View student unsuccessful - File Not Found : :")

    else:
        # Close the file and print a success message if the file is found
        file.close()
        print(": : View student successful : :")
