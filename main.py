import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

#Define Question Class
class Question:
    def __init__(self, question_text, answers, correct_answer):
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer

#DEFINE THE QUIZ CLASS TO MANAGE QUESTIONS BY DIFFICUTLY LEVEL
class Quiz:
    def __init__(self):
        self.questions = {
        'easy': [
                Question('Simplify the expression 3x + 5x', ['7x', '8x', '9x'], '8x'),
                Question('Simplify the expression 7y - 2y', ['5y', '6y', '9y'], '5y'),
                Question('Simplify the expression 4a + 6a', ['9a', '10a', '2a'], '10a'),
                Question('Simplify the expression 9b -3b + 2b', ['7x', '7b', '8b'], '8b'),
                Question('Simplify the expression 2m + 3m + 4m', ['8m', '9m', '10m'], '9m'),
                Question('Simplify the expression 5c - c', ['3c', '4c', '5c'], '4c'),
            ],
            'medium': [
                Question('Simplify the expression 3x + 5x', ['7x', '8x', '9x'], '8x'),
                Question('Simplify the expression 7y - 2y', ['5y', '6y', '9y'], '5y'),
                Question('Simplify the expression 4a + 6a', ['9a', '10a', '2a'], '10a'),
                Question('Simplify the expression 9b -3b + 2b', ['7x', '7b', '8b'], '8b'),
                Question('Simplify the expression 2m + 3m + 4m', ['8m', '9m', '10m'], '9m'),
                Question('Simplify the expression 5c - c', ['3c', '4c', '5c'], '4c'),
            ],
            'hard': [
                Question('Simplify the expression 3x + 5x', ['7x', '8x', '9x'], '8x'),
                Question('Simplify the expression 7y - 2y', ['5y', '6y', '9y'], '5y'),
                Question('Simplify the expression 4a + 6a', ['9a', '10a', '2a'], '10a'),
                Question('Simplify the expression 9b -3b + 2b', ['7x', '7b', '8b'], '8b'),
                Question('Simplify the expression 2m + 3m + 4m', ['8m', '9m', '10m'], '9m'),
                Question('Simplify the expression 5c - c', ['3c', '4c', '5c'], '4c'),
            ]
        }
 # Dictionary to store scores
        self.scores = {
            'easy': {'correct': 0, 'incorrect': 0},
            'medium': {'correct': 0, 'incorrect': 0},
            'hard': {'correct': 0, 'incorrect': 0}
        }

    def get_questions(self, difficulty):
        return self.questions[difficulty]

    def get_score(self, difficulty, result):
        return self.scores[difficulty][result]
        
    def update_score(self, difficulty, result):
        self.scores[difficulty][result] += 1

    def randomize_questions(self, difficulty):
        #THIS WILL SHUFFLE QUESTIONS DEPENDING ON THE DIFFICULTY LEVEL
        random.shuffle(self.questions[difficulty])


# Define the QuizApp class to manage the GUI and quiz flow
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize main window
        self.title('Quiz Application')
        self.geometry('1080x720')  

        #Insstance Variables for managing state
        self.current_page = 'start'  # Track current page of the application
        self.question_index = 0  # Track current question index in the quiz
        self.difficulty = None  # Store selected difficulty level
        self.name = ''  # Store user's name
        self.year_level = ''  # Store user's year level
        self.info_saved = False #track if users info has been saved 

        # Load and resize images for different screens
        self.page1_image = Image.open("page1.png").resize((1080, 720), Image.LANCZOS)
        self.page1_photo = ImageTk.PhotoImage(self.page1_image)

        self.page2_image = Image.open("page2.jpg").resize((1080, 720), Image.LANCZOS)
        self.page2_photo = ImageTk.PhotoImage(self.page2_image)

        self.dif_image = Image.open("dif.PNG").resize((1080, 720), Image.LANCZOS)
        self.dif_photo = ImageTk.PhotoImage(self.dif_image)

        self.sc_image = Image.open("SC.PNG").resize((1080, 720), Image.LANCZOS)
        self.sc_photo = ImageTk.PhotoImage(self.sc_image)

        # Create a canvas widget to draw UI elements
        self.canvas = tk.Canvas(self, width=1080, height=720)
        self.canvas.pack()

        #Initialize the quiz object
        self.quiz = Quiz()

        # Start with the initial start page 
        self.show_start_page()

    def show_start_page(self):
        self.canvas.delete('all')  # Clear the canvas

        #Display background image for the starting page
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.page1_photo)

        #Labels and the entry fieled for name and year level
        self.name_label = tk.Label(self.canvas, text='Enter your name:')
        self.name_label.place(x=400, y=320)  # Adjusted y and x coordinate
        self.name_entry = tk.Entry(self.canvas)
        self.name_entry.place(x=550, y=320)  # Adjusted y and x coordinate
        self.name_entry.bind('<KeyRelease>', self.limit_name_length)

        self.year_label = tk.Label(self.canvas, text='Enter your year level:')
        self.year_label.place(x=400, y=370)  # Adjusted y and x coordinate
        self.year_entry = tk.Entry(self.canvas)
        self.year_entry.place(x=550, y=370)  # Adjusted y and x coordinate
        self.year_entry.bind('<KeyRelease>', self.validate_year_level)

        #BUTTONS FOR GOING TO THE NEXT PAGE AND SAVING DETIALS
        self.save_button = tk.Button(self.canvas, text='Save', command=self.save_details)
        self.save_button.place(x=500, y=420)

        self.skip_button = tk.Button(self.canvas, text='Next', command=self.skip_start_page)
        self.skip_button.place(x=600, y=420)

        #Placeholder for error messages
        self.error_message = tk.Label(self.canvas text='', fg='red', bg='#FDDCC7', width=50, 
        height=2)
        self.error_message.place(x=400, y=460)


    
    def limit_name_length(self, event):
                                current_name = self.name_entry.get()
                                if any(char.isdigit() for char in current_name):
                                   messagebox.showerror("Input Error", "Please enter only letters.")
                                   self.name_entry.delete(0, tk.END)
                                elif any(not char.isalnum() and not char.isspace() for char in current_name):
                                    messagebox.showerror("Input Error", "Symbols are not allowed. Please enter only letters.")
                                    self.name_entry.delete(0, tk.END)
                                elif len(current_name) > 8:
                                    messagebox.showerror("Input Error", "Please enter a maximum of 8 letters.")
                                    self.name_entry.delete(8, tk.END)


                                def validate_year_level(self, event):
                                    current_year = self.year_entry.get()
                                if any(char.isalpha() for char in current_year):
                                   messagebox.showerror("Input Error", "Please enter only numbers.")
                                   self.year_entry.delete(0, tk.END)
                                elif any(not char.isdigit() for char in current_year):
                                     messagebox.showerror("Input Error", "Symbols are not allowed. Please enter only numbers.")
                                     self.year_entry.delete(0, tk.END)
                                elif len(current_year) > 2:
                                     messagebox.showerror("Input Error", "Please enter a maximum of 2 digits.")
                                     self.year_entry.delete(2, tk.END)

  
    def skip_start_page(self):
        self.error_message.config(text='')

        if not self.info_saved:
            self.error_message.config(text='Please make sure to save before skipping.')
            return
            
        #DESTORY NAME AND ENTRY WIDGETS AND ERROR MESSAGES
        self.error_message.destroy()
        self.name_label.destroy()
        self.name_entry.destroy()
        self.year_label.destroy()
        self.year_entry.destroy()
        self.save_button.destroy()
        self.skip_button.destroy()

        # Show difficulty selection page 
        self.show_difficulty_page()
        
    def save_details(self):
        self.name = self.name_entry.get()
        self.year_level = self.year_entry.get()

        if not self.name or not self.year_level:
            self.error_message.config(text='Both fields are required to save')
            return

        if len(self.name) > 8:
            self.error_message.config(text='Please only enter a max of 8 characters.')
            return

        if len(self.year_level) > 2:
            self.error_message.config(text='Please only enter a max of 2 digits for year 
            level.')
            return

        self.info_saved = True
        self.error_message.config(text='Information saved succefully. Feel free to skip
        now.')
        self.save_button.config(state=tk.DISABLED)

    def show_difficulty_page(self):
        self.canvas.delete('all')  # Clear canvas

        # Display background image for the difficulty page
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.dif_photo)

        # Create buttons for selecting difficulty levels
        button_font = ('Arial', 18, 'bold')
        button_width = 20
        button_height = 2

        easy_button = tk.Button(
            self.canvas, text='Easy', font=button_font, width=button_width, 
            height=button_height, 
            command=lambda: self.start_quiz('easy'), bg='white', fg='black',
            hightlightbackground='black'
        )
        easy_button.place(x=440, y=220)  

        medium_button = tk.Button(
            self.canvas, text='Medium', font=button_font, width=button_width, 
            height=button_height, 
            command=lambda: self.start_quiz('medium'), bg='white', fg='black', 
            highlightbackground='black'
        )
        medium_button.place(x=440, y=320)  # Adjusted y-coordinate

        hard_button = tk.Button(
            self.canvas, text='Hard', font=button_font, width=button_width, 
            height=button_height, 
            command=lambda: self.start_quiz('hard'), bg='white', fg='black', 
            highlightbackground='black'
        )
        hard_button.place(x=620, y=420) # Adjusted y-coordinate

    def start_quiz(self, difficulty): 
        self.current_page = 'quiz'
        self.difficulty = difficulty
        self.question_index = 0

        # Clear canvas
        for widget in self.canvas.winfo_children():
            widget.destroy()

        # Shuffle questions for selected difficulty
        self.quiz.randomize_questions(difficulty)
        self.show_question() #DISPLAY THE FIRST QUESTION

            def show_question(self):
                                 if self.question_index < 
len(self.quiz.get_questions(self.difficulty)):
                            self.canvas.delete('all') # Clear canvas

            # Display background image for quiz
                            self.canvas.create_image(0, 0, anchor=tk.NW, 
                            image=self.dif_photo)

            # Retrieve question data
            question_data = quiz.get_questions(self.difficulty)[self.question_index]
            question_text = question_data.question_text
            answers = question_data.answers
            correct_answer = question_data.correct_answer

            #Create a label with a white background and black border
            question
            question_label = tk.Label(
               self.canvas,
               text=question_text,
               font=('Playwrite Cuba', 20, 'bold'),
               bg='white',
               highlightbackground='black',
               highlightthickness=1
            )                         
            question_label.place(x=50m y=300) #adjust where the question goes

           # Display answer buttons
            self.answer_buttons = []
            for i, answer in enumerate(answers):
                button = tk.Button(
                    self.canvas,
                    text=answer,
                    font=('Arial', 10)
                    bg='white',
                    highlightbackground='black', 
                    highlightthickness=1, 
                    command=lambda ans=answer: self.check_answer(ans,
                    correct_answer)                
                )                                                
                button.place(x=110, y=390 + i * 50)
                self.answer_buttons.append(button)
                                    
            self.question_index += 1  # Move to the next question index
        else:
            # All questions answered, show scoreboard
            self.show_scoreboard()

        def check_answer(self, selected_answer, correct_answer):
            if selected_answer == correct_answer:
                self.quiz.update_score(self.difficulty, 'correct')
            else:
                self.quiz.update_score(self.difficulty, 'incorrect')

            for widget in self.canvas.winfo_children():
                if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                    widget.destroy()

            self.show_question()

    def show_scoreboard(self):
        self.current_page = 'scoreboard'
        self.canvas.delete('all')  # Clear canvas

        # Display background image for scoreboard
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.sc_photo)

        #PERONSALIZED MESSAHE WITH TEXT WRAPPING
        thank_you_message = (
            f"Thanks for taking the quiz, {self.name}! You got "
            f"{self.quiz.get_scores(self.difficulty, 'correct')} correct and "
            f"{self.quiz.get_scores(self.difficulty, 'incorrect')} incorrect."
        )
        year_level_message = f"Good luck in year  {self.year_level}!"

        # create labels with text wrapping
tk.Label(
    self.canvas,
    text=thank_you_message,
    font=('Helvetica', 18),
    wraplength=800,  
    justify=tk.CENTER
).place(x=100, y=200)  

tk.Label(
    self.canvas,
    text=year_level_message,
    font=('Arial', 18),
    wraplength=800,  
    justify=tk.CENTER
).place(x=100, y=265)  

restart_button = tk.Button(
    self.canvas, 
    text='Restart!', 
    command=self.restart_quiz, 
    bg='white', 
    highlightbackground='black', 
    highlightthickness=1,
    font=('Arial', 13),
    width=9,
    height=2
)
restart_button.place(x=100, y=340)

def restart_quiz(self):
    self.question_index=0
    self.quiz.scores[self.difficulty]['correct'] = 0
    self.quiz.scores[self.difficulty]['incorrect'] = 0

    for widget in self.canvas.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.destroy()

    self.show_difficulty_page()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()