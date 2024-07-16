from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#fff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

REPEATS = 1
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #
# class PomodoroTimer(Frame):
#     def __init__(self):
#         Frame.__init__(self)
def reset_timer():
    if TIMER is not None:
        window.after_cancel(TIMER)

    global REPEATS
    REPEATS = 0

    check_mark.config(text="")
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPEATS

    work_span = WORK_MIN * 60
    short_break_span = SHORT_BREAK_MIN * 60
    long_break_span = LONG_BREAK_MIN * 60

    if REPEATS % 8 == 0:
        count_down(long_break_span)
        title.config(text="Long Break")
        check_mark.config(text="")
    elif REPEATS % 2 == 0:
        count_down(short_break_span)
        title.config(text="Short Break")
        check_mark.config(text=check_mark.cget("text")+"✔")
    else:
        count_down(work_span)
        title.config(text="Work Time")
    REPEATS += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = count // 60  # math.floor(count / 6)
    seconds = count % 60

    if minutes < 10:
        minutes = "0" + str(minutes)

    if seconds < 10:
        seconds = "0" + str(seconds)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=40, pady=20)

tomato_img = PhotoImage(file="tomato.png")

title = Label(window, text="Timer", fg=WHITE, font=(FONT_NAME, 40, "bold"))
title.grid(row=0, column=1)

start_button = Button(window, text="Start", fg=PINK, command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(window, text="Reset", fg=PINK, command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(window, text="", fg=PINK)
check_mark.grid(column=1, row=4)

canvas = Canvas(window, width=280, height=280, highlightthickness=0)
canvas.create_image(143, 140, image=tomato_img)
timer_text = canvas.create_text(143, 160, text="00:00", fill=WHITE, font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
