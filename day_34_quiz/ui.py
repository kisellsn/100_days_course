from tkinter import *

from day_34_quiz.quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(self.window, text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, bg="white", width=300, height=250)
        self.question = self.canvas.create_text(150, 140,
                                                text="",
                                                font=("Ariel", 20, "italic"),
                                                fill="black",
                                                width=280,
                                                anchor=CENTER)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(self.window, image=true_img,
                                  width=100, height=100,
                                  highlightthickness=0, command=self.true_guess)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(self.window, image=false_img,
                                   width=100, height=100,
                                   highlightthickness=0, command=self.false_guess)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question,
                                   text=f"You finished the game! Finally score {self.quiz.score}")
            self.score_label.config(text="")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_guess(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_guess(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



