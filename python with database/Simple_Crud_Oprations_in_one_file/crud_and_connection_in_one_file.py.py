import pymysql

# Connect to MySQL server
mydb = pymysql.connect(user="root", host="localhost", passwd="")
mycursur = mydb.cursor()

# Create database if it doesn't exist
mycursur.execute("CREATE DATABASE IF NOT EXISTS crud2")

# Connect to the 'crud2' database
mydb = pymysql.connect(user="root", host="localhost", passwd="", database="crud2")
mycursur = mydb.cursor()

# Create table if it doesn't exist
mycursur.execute("""
CREATE TABLE IF NOT EXISTS c_info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    city VARCHAR(20)
)
""")
mydb.commit()

# Menu options
menu = """
    Press 1 for adding a student
    Press 2 for updating a student
    Press 3 for deleting a student
    Press 4 for searching a student
    Press 5 for searching all students
"""

# Function to add a student
def add():
    name = input("Enter name: ")
    city = input("Enter city: ")
    args=(name,city)
    query = "INSERT INTO c_info (name, city) VALUES (%s, %s)"
    mycursur.execute(query%args)
    mydb.commit()
    print("Successfully added!")

# Function to update a student
def update():
    try:
        id = int(input("Enter ID to update: "))
        # Check if the ID exists in the database
        query = "SELECT * FROM c_info WHERE id = %s"
        mycursur.execute(query, (id,))
        data = mycursur.fetchone()
        if not data:
            print("No student found with the given ID. Please try again.")
            return

        name = input("Enter name: ")
        city = input("Enter city: ")
        query = "UPDATE c_info SET name = %s, city = %s WHERE id = %s"
        mycursur.execute(query, (name, city, id))
        mydb.commit()
        print("Successfully updated!")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
    
# Function to delete a student
def delete():
    try:
        id = int(input("Enter ID to delete: "))
        # Check if the ID exists in the database
        query = "SELECT * FROM c_info WHERE id = %s"
        args=(id)
        mycursur.execute(query%args)
        data = mycursur.fetchone()
        if not data:
            print("No student found with the given ID. Please try again.")
            return

        query = "DELETE FROM c_info WHERE id = %s"
        mycursur.execute(query%args)
        mydb.commit()
        print("Successfully deleted!")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

# Function to search for a student
def search():
    id = int(input("Enter ID to search: "))
    query = "SELECT * FROM c_info WHERE id = %s"
    args=(id)
    mycursur.execute(query%args)
    data = mycursur.fetchone()
    if data:
        print(f"ID: {data[0]}, Name: {data[1]}, City: {data[2]}")
    else:
        print("No student found with the given ID.")
    mydb.commit()

# Function to search for all students
def searchall():
    query = "SELECT * FROM c_info"
    mycursur.execute(query)
    data = mycursur.fetchall()
    for row in data:
        print(f"ID: {row[0]}, Name: {row[1]}, City: {row[2]}")
    mydb.commit()
    print("Successfully searched all students!")

# Main loop
status = True
while status:
    print(menu)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        update()
    elif choice == 3:
        delete()
    elif choice == 4:
        search()
    elif choice == 5:
        searchall()
    else:
        print("Invalid choice, please try again.")

    u_choice = input("Do you want to perform more operations? (y for yes, n for no): ").lower()
    if u_choice == 'n':
        status = False
    elif u_choice != 'y':
        print("Invalid input, exiting the program.")
        status = False

print("Goodbye!")
