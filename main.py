import tkinter as tk
from PIL import Image, ImageTk

def save_details():
    name = name_entry.get()
    year_level = year_entry.get()
    print("Name:", name)
    print("Year Level:", year_level)
    name_entry.delete(0, "end")
    year_entry.delete(0, "end")

def skip_next_page():
    print("Skipping to next page...")  # i will  add implementation here

def resize_image(event):
    global resized_image, photo
    new_width = event.width
    new_height = event.height
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=new_width, height=new_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

root = tk.Tk()
root.geometry("800x600")
root.title("Image Display")

# Load the original image
image_path = "page1.png"
original_image = Image.open(image_path)

# Resize the original image to fit the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
aspect_ratio = original_image.width / original_image.height
if aspect_ratio > screen_width / screen_height:
    new_width = screen_width
    new_height = int(screen_width / aspect_ratio)
else:
    new_height = screen_height
    new_width = int(screen_height * aspect_ratio)
original_image = original_image.resize((new_width, new_height), Image.LANCZOS)

# Create canvas to display the image
canvas = tk.Canvas(root, width=new_width, height=new_height, highlightthickness=0, bd=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Display the image on the canvas
photo = ImageTk.PhotoImage(original_image)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Add labels and entry fields directly on top of the canvas
label_color = '#f5deb3' #LIGHT SKIN COLOUR as my users said it would look much better

name_label = tk.Label(root, text="Enter your name:")
name_label.place(relx=0.5, rely=0.45, anchor="center")
name_entry = tk.Entry(root)
name_entry.place(relx=0.5, rely=0.5, anchor="center")
year_label = tk.Label(root, text="Enter your year level:")
year_label.place(relx=0.5, rely=0.55, anchor="center")
year_entry = tk.Entry(root)
year_entry.place(relx=0.5, rely=0.6, anchor="center")

# Create frame for buttons with a very light background color
button_frame = tk.Frame(root, bg=label_color)  # Light gray color
button_frame.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Add save button with black outline
save_button = tk.Button(button_frame, text="Save Details", command=save_details, 
                        bg=label_color, activebackground=label_color, 
                        highlightthickness=1, highlightbackground="black", bd=0)
save_button.pack(side=tk.LEFT, padx=5)
        
# Add skip/next page button with black outline
skip_button = tk.Button(button_frame, text="Skip/Next Page", command=skip_next_page, 
bg=label_color, activebackground=label_color, 
highlightthickness=1, highlightbackground="black", bd=0) 
skip_button.pack(side=tk.LEFT, padx=5)


# Bind the resize function to the root window
root.bind("<Configure>", resize_image)

root.mainloop()


