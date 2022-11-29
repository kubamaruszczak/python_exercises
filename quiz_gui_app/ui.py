from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RIGHT_COLOR = "#29B677"
WRONG_COLOR = "#EC645C"

Q_FONT = ("Arial", 20, "italic")
S_FONT = ("Arial", 12)


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=S_FONT)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.question_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=Q_FONT, width=280)
        self.get_next_question()

        # True button
        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img,
                                  highlightthickness=0,
                                  bg=THEME_COLOR,
                                  command=self.choose_true)
        self.true_button.grid(row=2, column=0)

        # False button
        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img,
                                   highlightthickness=0,
                                   bg=THEME_COLOR,
                                   command=self.choose_false)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            final_msg = f"You've completed the quiz. " \
                        f"Your final score is: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, text=final_msg)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def choose_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def choose_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=RIGHT_COLOR)
        else:
            self.canvas.config(bg=WRONG_COLOR)
        self.window.after(1000, func=self.get_next_question)
