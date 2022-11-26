from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FRONT_TEXT_COLOR = "black"
BACK_TEXT_COLOR = "white"
FONT_NAME = "Arial"

current_card = {}
flash_timer = None


def next_card():
    global current_card, flash_timer

    if flash_timer is not None:
        window.after_cancel(flash_timer)

    # Change the card image to front
    canvas.itemconfig(card_image, image=card_front_img)

    # Get a random word - translation pair and update front card texts
    if len(to_learn) > 1:
        current_card = random.choice(to_learn)
        canvas.itemconfig(title_text, text="French", fill=FRONT_TEXT_COLOR)
        canvas.itemconfig(word_text, text=current_card["French"], fill=FRONT_TEXT_COLOR)

        flash_timer = window.after(3000, flip_card)
    else:
        messagebox.showinfo(title="Info", message="You've know all the words from actual set!")


def is_known():
    if current_card in to_learn:
        to_learn.remove(current_card)
        to_learn_df = pandas.DataFrame(to_learn)
        to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill=BACK_TEXT_COLOR)
    canvas.itemconfig(word_text, text=current_card["English"], fill=BACK_TEXT_COLOR)


# Read words with translations from the appropriate file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# --------------------- UI ---------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)

title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
red_button_img = PhotoImage(file="images/wrong.png")
red_button = Button(image=red_button_img, highlightthickness=0, command=next_card)
red_button.grid(row=1, column=0)

green_button_img = PhotoImage(file="images/right.png")
green_button = Button(image=green_button_img, highlightthickness=0, command=is_known)
green_button.grid(row=1, column=1)

next_card()

window.mainloop()
