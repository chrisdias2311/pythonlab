import tkinter as tk

# create a new tkinter window
root = tk.Tk()
root.title("Login Page")

# define a function to verify the user's credentials
def login():
    # get the values entered in the username and password fields
    username = username_entry.get()
    password = password_entry.get()
    
    # check if the username and password are correct
    if username == "admin" and password == "password":
        result_label.config(text="Login successful!")
    else:
        result_label.config(text="Login failed.")

# create labels and entry fields for the username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# create a button to submit the login credentials
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# create a label to display the login result
result_label = tk.Label(root)
result_label.pack()

# start the tkinter event loop
root.mainloop()