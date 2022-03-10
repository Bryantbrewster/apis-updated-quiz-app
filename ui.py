from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(height=550, width=400)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(self.window, bg='white', width=300, height=250)
        self.canvas.place(x=30, y=100)
        self.blank_label = Label(text="Score:", highlightthickness=0)
        self.blank_label.place(x=225, y=50)
        self.question_text = self.canvas.create_text(150, 100, text='Question Text', width=280, font=('Arial', 20, 'italic'))
        self.checkmark = PhotoImage(file='./images/true.png')
        self.green_button = Button(self.window, width=80, height=80, image=self.checkmark, highlightthickness=0, command=self.check_if_true)
        self.green_button.place(x=225, y=400)
        self.x_pic = PhotoImage(file='./images/false.png')
        self.red_button = Button(self.window, width=80, height=80, image=self.x_pic, highlightthickness=0, command=self.check_if_false)
        self.red_button.place(x=50, y=400)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.blank_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")


    def check_if_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def check_if_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)