import tkinter as tk
from PIL import Image, ImageTk

# Start the initial start page
self.show_start_page()

def show_start_page(self):

    self.canvas.delete('all')

#Display background image for the starting page
self.canvas.create_image(0,0, anchor=tk.NW, image=self.page1_photo)

#Lavels and the entry fieled for name and year level
self.name_label = tk.Label(self.canvas, text='Enter your name:')
self.name_label.place(x=400, y=320) #ADJUST THE Y COORDINATE
self.name_entry = tk.Entry(self.canvas)
self.name_entey.place(x=550, y=370) #ADJUST y COORDINATE

self.year_label= tk.Label(self.canvas, text='Enter your year level:')
self.year_label.place(x=400, y=370)
self.year_entry = tk.Entry(self.canvas)
self.year_entry.place(x=550, y=370)

#BUTTONS FOR SKIPPING AND SAVING DETIALS
tk.Button(self.canvas, text'Skip', command=self.skip_start_page). place(x=500, y=420)

tk.Button(self.canvas, text='Save', command=self.save_details).place(x=600, y=420)

def skip_start_page(self):

#DESTORY NAME AND ENTRY WIDGETS
self.name_label.destroy()
self.name_entry.destroy()
self.year_lebel.destory()
self.year_entry.destory()

#Remove buttons from the canvas
for widget in self.canvas.winfo_children():
    if isinstance(widget, tk.Button):
        widget.destory()

#Show difficutly selection page (2nd page)
self.show_difficutly_page()

def save_details(self):

    self.name = self.name_entry.get()
    self.year_level = self.year_entry.get()

#destroy name and year entry widgets
self.name_label.destroy()
self.name_entry.destroy()
self.year_label.destroy()
self.year_entry.destroy()

    


