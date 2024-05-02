print(" LOGIN FORM GUI WITH PYTHON")


# Importing modules
import tkinter as tk
from tkinter import messagebox 
from PIL import ImageTk, Image

root = tk.Tk() # Create the main Tkinter window
root.title("LOGIN FORM BY ISAAR") # Set the title of the window
root.iconbitmap(r"C:\Users\dell\Desktop\python_GUI\1.folder\flipkart_icon-icons.com_62782.ico") # Set the window icon
root.geometry("400x500") # Set the size of the window
root.configure(background="#0096DC") # Set the background color of the window

# This function handles the login process
def handel_login():
    email = email_input.get()
    password = password_input.get()

    if email == "isaar@gmail.com" and password == "12345":
        messagebox.showinfo("Success", "Login Successful") 
    else:
        messagebox.showerror("Error", "Login Failed")

# Load and resize image
img = Image.open(r"C:\Users\dell\Desktop\python_GUI\1.folder\flipkart-logo.png")
resized_img = img.resize((100, 100))
img = ImageTk.PhotoImage(resized_img)

# Display the logo image
img_label = tk.Label(root, image=img)
img_label.pack(pady=(30, 0))

# Label for the company name
text_label = tk.Label(root, text="FlipKart", fg="white", bg="#0096DC", font=("verdana", 24))
text_label.pack()

# Label and entry field for email input
email_label = tk.Label(root, text="ENTER EMAIL:", fg="white", bg="#0096DC", font=("verdana", 13))
email_label.pack(pady=(20, 5))
# Entry field for email input
email_input = tk.Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

# Label and entry field for password input
password_label = tk.Label(root, text="ENTER PASSWORD:", fg="white", bg="#0096DC", font=("verdana", 13))
password_label.pack(pady=(20, 5))
# Entry field for password input
password_input = tk.Entry(root, width=50)
password_input.pack(ipady=6, pady=(1, 15))

# Button for login action
login_btn = tk.Button(root, text="LOGIN HERE", bg="white", fg="black", width=20, height=2, command=handel_login, font=("verdana", 10))
login_btn.pack(pady=(10, 20))

# This starts the GUI application and handles user interactions
root.mainloop()
