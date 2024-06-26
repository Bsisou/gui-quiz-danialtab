import tkinter as tk
from PIL import Image, ImageTk
import random

#Define Question Class
class Question:
def __init__(self, question_text, answers, correct_answer):
    self.question_text = question_text
    self.answeres = answers
    self.correct_answer = correct_answer

#DEFINE THE QUIZ CLASS TO MANAGE QUESTIONS BY DIFFICUTLY LEVEL
class Quiz:
    def __init__(self):
        self.questions = {
            'easy' [
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
      ],
        }

#Dictonary to store scores
self.scores = {
    'easy': {'correct': 0, 'incorrect': 0},
    'medium': {'correct': 0, 'incorrect': 0}
    'hard': {'correct': 0, 'incorrect': 0}
}


        
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

3(self, difficutly):

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

# retrive question data
question_data = quiz.get_questions(self.difficulty)[self.question_index]
question_text = question_data.question_text
answers = question_data.answers
correct_answer = question_data.correct_answer

# display question title
question_label = tk.Label(self.canvas, text=queastion_text, font=('Helvetica', 18, 'bold'))
question_label.place(x-100, y=180) # Y COORDINATE

# display awnser buttons 
self.answer_buttons = []
for i, answer in enumerate(answers):
    button =tk.Button(self.canvas, text=answer, command=lambda ans=answer:
 self.check_answer(ans, correct_answer))
    button.place(x=100, y=240 + i * 50) 
    self.answer_buttons.append(button)

    self.question_index += 1 # move to the next question index
else:
    # all questistions have been awnsered now the scourbourd will show
    self.show_scoreboard()

def check_answer(self, selected_answer, correct_answer):

if selected_answer == correct_answer:
    quiz.update_score(self.difficulty, 'correct')
else:
    quiz.update_score(self.difficulty, 'incorrect')

    #clear canvas
    for widget in self.canvas.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.destroy()

            #Display the next question or scourbouard
            self.show_question()

            def show_scorebourd(self):

                self.current_page = 'scoreboard'
                self.canvas.delete('all') #Clear Canvas

            #Display background image for scourbourd
            self.canvas.create_image(0, 0, anchor=tl.NW, image=self.sc_photo)

            #Display scoreboard labels
tk.Label(self.canvas, text='Scoreboard', font=('Helvetica', 24, 'bold')).place(x=400, y=180)  
tk.Label(self.canvas, text=f'Correct: {quiz.get_score(self.difficulty, "correct")}', font=('Helvetica', 18)).place(x=400, y=280)  
tk.Label(self.canvas, text=f'Incorrect: {quiz.get_score(self.difficulty, "incorrect")}', font=('Helvetica', 18)).place(x=400, y=330)
                                                            
#Button to restart the quiz at the end
restart_button = tk.Button(self.canvas, text='Restart', command=self.restart_quiz)
restart_button.place(x=500, y=440)

def restart_quiz(self):

    self.questions_index = 0
    quiz.scores[self.difficulty]['correct'] = 0
    quiz.scores[self.difficulty]['incorrect'] = 0

 #Clear Scorebourd and the restart button when the restart button is clicked 
for widget in self.canvas.winfo_children():
    if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
        widget.destroy()

 #Show Difficutly selecton page 
self.show_difficulty_page()

if __name__ == "__main__":
    quiz = Quiz()
    app = QuizApp()
    app.mainloop()
