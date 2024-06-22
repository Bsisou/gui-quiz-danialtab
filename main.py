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

def show_difficulty_page(self):

    self.canvas.delete('all')

# Display Background image for the difficutly selection page (2nd page)
self.canvas.create_image(0,0, anchor=tk.NW, image=self.page2_photo)

# create buttons for selecting diffuclty levels
button_font = ('helvetica' 18)
button_width = 20 
button_height = 2

easy_button = tk.Button(self.canvas, text='Easy', font=button_font,
width=button_width, height=button_height, command=lamba :self.start_quiz('easy'))
easy_button.place(x=440, y=220) # Y COORDINGATNE 

medium-button = tk.Button(self.canvas, text='Medium', font=button_font,
width=button_width, height=button_height, command=lambda: self.start_quiz('medium'))
medium_button.place(x=440, y=420) # Y COORDINGINATE

def start_quiz(self, difficutly):

    self.current_page= 'quiz'
    self.difficutly = difficutly
    self.question_index = 0

#clear canvas
for widget in self.canvas.winfow_children():
    widget.destroy()

# shuffle questions for selected difficutly
quiz.randomize_questions(difficulty)

# display the first question 
self.show_questions()

def show_questions(self):

    if self.quetsions_index < len(quiz.get_questions(self.difficutly)):
        self.canvas.delete('all') # clear CANVAS

# Display background image for quiz
self.canvas.create_image(0, 0 anchor=tk.NW, image=self.dif_photo)

# 