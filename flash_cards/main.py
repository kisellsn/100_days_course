import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_pair = {}
TIMER = None
# ---------------------------- LOAD WORDS ------------------------------- #

try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data = pandas.read_csv("data/pl-eng.csv")

to_learn = words_data.to_dict(orient="records")

# ---------------------------- NEXT CARD ------------------------------- #


def send_to_learned():
    global to_learn
    to_learn.remove(current_pair)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def save_for_later():
    next_card()


def next_card():
    global current_pair, TIMER
    if TIMER is not None:
        window.after_cancel(TIMER)

    current_pair = random.choice(to_learn)

    canvas.itemconfig(canvas_img, image=card_front)
    canvas.itemconfig(language_text, text="Polish", fill="black")
    canvas.itemconfig(word_text, text=current_pair["Polish"], fill="black")

    TIMER = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_pair["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(window, width=800, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = canvas.create_image(400, 300, image=card_front)
language_text = canvas.create_text(400, 120, text="Language", font=(FONT_NAME, 40, "italic"), fill="black")
word_text = canvas.create_text(400, 300, text="WORD", font=(FONT_NAME, 60, "bold"), fill="black")

canvas.grid(column=0, row=0, columnspan=3)



# BUTTONS
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, border=0, command=send_to_learned)
right_btn.grid(column=2, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, border=0, command=save_for_later)
wrong_btn.grid(column=0, row=1)


next_card()

window.mainloop()