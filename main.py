import tkinter as tk
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
        """Shuffle questions for the specified difficulty level."""
        random.shuffle(self.questions[difficulty])


# Define the QuizApp class to manage the GUI and quiz flow
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize main window
        self.title('Quiz Application')
        self.geometry('1080x720')  

        self.current_page = 'start'  # Track current page of the application
        self.question_index = 0  # Track current question index in the quiz
        self.difficulty = None  # Store selected difficulty level
        self.name = ''  # Store user's name
        self.year_level = ''  # Store user's year level

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

        # Start with the initial start page 
        self.show_start_page()

    def show_start_page(self):

        self.canvas.delete('all')  # Clear canvas

        #Display background image for the starting page
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.page1_photo)

        #Labels and the entry fieled for name and year level
        self.name_label = tk.Label(self.canvas, text='Enter your name:')
        self.name_label.place(x=400, y=320)  # Adjusted y-coordinate
        self.name_entry = tk.Entry(self.canvas)
        self.name_entry.place(x=550, y=320)  # Adjusted y-coordinate
        self.name_entry.bind('<KeyRelease>', self.limit_name_length)

        self.year_label = tk.Label(self.canvas, text='Enter your year level:')
        self.year_label.place(x=400, y=370)  # Adjusted y-coordinate
        self.year_entry = tk.Entry(self.canvas)
        self.year_entry.place(x=550, y=370)  # Adjusted y-coordinate
        self.year_entry.bind('<KeyRelease>', self.validate_year_level)

        #BUTTONS FOR GOING TO THE NEXT PAGE AND SAVING DETIALS
        tk.Button(self.canvas, text='Next', command=self.skip_start_page).place(x=500, y=420) 
        tk.Button(self.canvas, text='Save', command=self.save_details).place(x=600, y=420)  

    def limit_name_length(self, event):
        current_name = self.name_entry.get()
        if len(current_name) > 8:
            self.name_entry.delete(8, tk.END)

    def validate_year_level(self,event):
        current_year = self.year_entry.get()
        if len(current_year) > 2 or not current_year.isdigit():
            self.year_entry.delete(2, tk.END) #THIS WILL LIMIT THE YEAR LEVEL to 2 DIFITS AND ENSURE ITS NUMERIC

    def skip_start_page(self):

        #DESTORY NAME AND ENTRY WIDGETS
        self.name_label.destroy()
        self.name_entry.destroy()
        self.year_label.destroy()
        self.year_entry.destroy()

        # Remove buttons from canvas
        for widget in self.canvas.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        # Show difficulty selection page 
        self.show_difficulty_page()

    def save_details(self):

        self.name = self.name_entry.get()
        self.year_level = self.year_entry.get()

        # Destroy name and year entry widgets
        self.name_label.destroy()
        self.name_entry.destroy()
        self.year_label.destroy()
        self.year_entry.destroy()

    def show_difficulty_page(self):

        self.canvas.delete('all')  # Clear canvas

        # Display background image for the difficulty page
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.page2_photo)

        # Create buttons for selecting difficulty levels
        button_font = ('Helvetica', 18)
        button_width = 20
        button_height = 2

        easy_button = tk.Button(self.canvas, text='Easy', font=button_font, width=button_width, 
        height=button_height, command=lambda: self.start_quiz('easy'))
        easy_button.place(x=440, y=220)  

        medium_button = tk.Button(self.canvas, text='Medium', font=button_font, width=button_width, 
        height=button_height, command=lambda: self.start_quiz('medium'))
        medium_button.place(x=440, y=320)  # Adjusted y-coordinate

        hard_button = tk.Button(self.canvas, text='Hard', font=button_font, width=button_width, height=button_height, command=lambda: self.start_quiz('hard'))
        hard_button.place(x=440, y=420)  # Adjusted y-coordinate

    def start_quiz(self, difficulty): 
        self.current_page = 'quiz'
        self.difficulty = difficulty
        self.question_index = 0

        # Clear canvas
        for widget in self.canvas.winfo_children():
            widget.destroy()

        # Shuffle questions for selected difficulty
        quiz.randomize_questions(difficulty)

        # Display the first question
        self.show_question()

    def show_question(self):

        if self.question_index < len(quiz.get_questions(self.difficulty)):
            self.canvas.delete('all')  # Clear canvas

            # Display background image for quiz
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.dif_photo)

            # Retrieve question data
            question_data = quiz.get_questions(self.difficulty)[self.question_index]
            question_text = question_data.question_text
            answers = question_data.answers
            correct_answer = question_data.correct_answer

            # Display question title
            question_label = tk.Label(self.canvas, text=question_text, font=('Helvetica', 18, 'bold'))
            question_label.place(x=100, y=180)  # Adjusted y-coordinate

            # Display answer buttons
            self.answer_buttons = []
            for i, answer in enumerate(answers):
                button = tk.Button(self.canvas, text=answer, command=lambda ans=answer: self.check_answer(ans, correct_answer))
                button.place(x=100, y=240 + i * 50)  # Adjusted y-coordinate
                self.answer_buttons.append(button)

            self.question_index += 1  # Move to the next question index
        else:
            # All questions answered, show scoreboard
            self.show_scoreboard()

    def check_answer(self, selected_answer, correct_answer):

        if selected_answer == correct_answer:
            quiz.update_score(self.difficulty, 'correct')
        else:
            quiz.update_score(self.difficulty, 'incorrect')

        # Clear canvas
        for widget in self.canvas.winfo_children():
            if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                widget.destroy()

        # Display the next question or scoreboard
        self.show_question()

    def show_scoreboard(self):

        self.current_page = 'scoreboard'
        self.canvas.delete('all')  # Clear canvas

        # Display background image for scoreboard
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.sc_photo)

        # Display scoreboard labels
        tk.Label(self.canvas, text='Scoreboard', font=('Helvetica', 24, 'bold')).place(x=400, y=180)  
        tk.Label(self.canvas, text=f'Correct: {quiz.get_score(self.difficulty, "correct")}', font=('Helvetica', 18)).place(x=400, y=280)  
        tk.Label(self.canvas, text=f'Incorrect: {quiz.get_score(self.difficulty, "incorrect")}', font=('Helvetica', 18)).place(x=400, y=330)  

        # Button to restart quiz
        restart_button = tk.Button(self.canvas, text='Restart', command=self.restart_quiz)
        restart_button.place(x=500, y=440)  # Adjusted y-coordinate

    def restart_quiz(self):

        self.question_index = 0
        quiz.scores[self.difficulty]['correct'] = 0
        quiz.scores[self.difficulty]['incorrect'] = 0

        # Clear scoreboard and restart button
        for widget in self.canvas.winfo_children():
            if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                widget.destroy()

        # Show difficulty selection page
        self.show_difficulty_page()


if __name__ == "__main__":
    quiz = Quiz()  # Instantiate the Quiz class
    app = QuizApp()
    app.mainloop()
