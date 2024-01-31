# from tkinter import *
# root = Tk()
# root.geometry("1000x450")
# root.resizable(False,False)
# frame1 = Frame(root, highlightbackground="black", highlightthickness=2)
# frame1.pack(padx=20, pady=8)

# C1 = Label(frame1, text = "YOU CLICKED ON      :          CHECK IN ", width=500, anchor="w",font=('Copperplate',30,'bold'))
# C1.pack(padx=110, pady=0)

# frame1 = Frame(root, highlightbackground="black", highlightthickness=2)
# frame1.pack(padx=20, pady=0)
# name = Label(frame1,text='Enter Name : ',font=('arial',12,'bold'))
# name.pack(padx=30,pady=10)
# e_name = Entry(frame1,text='Enter Name : ')
# e_name.pack(padx=30,pady=10)
# root.mainloop()
import tkinter as tk

def login():
    # Placeholder function for login validation
    print("Login button clicked.")

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("1000x400")
root.resizable(False, False)

# Header Frame
header_frame = tk.Frame(root, height=50,highlightbackground="black", highlightthickness=2)
header_label = tk.Label(header_frame, text="YOU CLICKED ON         :         CHECK  IN", font=("Copperplate", 30))
header_label.pack(side="top", padx=10, pady=10)
header_frame.pack(fill="x",padx=20, pady=8)

# Main Content Frame
main_frame = tk.Frame(root, pady=20)
username_label = tk.Label(main_frame, text="Username:")
username_entry = tk.Entry(main_frame)

password_label = tk.Label(main_frame, text="Password:")
password_entry = tk.Entry(main_frame, show="*")

login_button = tk.Button(main_frame, text="Login", command=login)

username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
login_button.grid(row=2, column=1, pady=10)

main_frame.pack()

# Footer Frame
footer_frame = tk.Frame(root, bg="blue", height=30)
footer_label = tk.Label(footer_frame, text="© 2024 Your Company", font=("Arial", 10), fg="white", bg="blue")
footer_label.pack(side="left", padx=10, pady=5)
footer_frame.pack(fill="x", side="bottom")

# Start the main event loop
root.mainloop()





