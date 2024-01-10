import counsellor

# Function to display options for the student
def display():
    print("\t\t1. View Our Result")
    print("\t\t2. Back to Main Menu")

#=========================View Our Result function==============================

def view_our_result():
    try:
        # Opening the file in read mode
        file = open("counsellor.txt", "r")

        # Reading the first line of the file
        data = file.readline()

        # Converting the content to a dictionary using eval
        content = eval(data)

        # Taking input for the serial number to view the result
        s_no = int(input("Enter serial number to view your result: "))

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
            print("Your result:", specific_student)
        else:
            print(": : Student not found : :")

    except FileNotFoundError:
        # Handling the case where the file is not found
        print("File Not Found")
