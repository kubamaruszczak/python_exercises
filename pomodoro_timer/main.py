from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 0
timer = None


# ---------------------------- DIFFERENT FUNCTIONS ------------------------------- #
def raise_above_all(tk_window):
    tk_window.attributes('-topmost', True)
    tk_window.update()
    tk_window.attributes('-topmost', False)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps == 8:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        reps = 0
    else:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer

    count_min = floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        raise_above_all(window)
        start_timer()

        marks = ""
        for _ in range(floor(reps / 2)):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# bg color can be set with hex code
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 138, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# Timer label
title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# Checkmarks label
check_marks = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

# Start button
start_button = Button(text="Start", font=(FONT_NAME, 10), bg="white", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 10), bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
