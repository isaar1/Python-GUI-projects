# Printing a title
print("WALLPAPER GUI BY USING PYTHON TKINTER MODULE")

# Importing necessary modules
import tkinter as tk
from PIL import ImageTk, Image
import os 

def rotate_image():
    global counter
    img_label.config(image = img_array[counter%len(img_array)])
    counter = counter + 1

counter = 1
# Creating the Tkinter root window
root = tk.Tk()
root.title("Wallpaper Viewer GUI")
root.iconbitmap(r"C:\Users\dell\Desktop\python_GUI\2.folder\eye.ico")
root.geometry("400x550")
root.config(bg="black")

# List files in the wallpapers directory
files = os.listdir(r"C:\Users\dell\Desktop\python_GUI\2.folder\wallpapers")
img_array = []

# Iterate over the files in the directory
for file in files:
    # Open each image file
    img = Image.open(os.path.join(r"C:\Users\dell\Desktop\python_GUI\2.folder\wallpapers", file))
    # Resize the image (fixing the resize method)
    resized_img = img.resize((200, 400))
    # Convert the image to PhotoImage object
    img_array.append(ImageTk.PhotoImage(resized_img))

# display img
img_label = tk.Label(root, image = img_array[0])
img_label.pack(pady=(55,10)) #to fit on screen


# button 
nxt_btn = tk.Button(root, text="Next", bg="white", fg="black", width=28, height=2, command=rotate_image)
nxt_btn.pack()
# Run the Tkinter event loop
root.mainloop()
