from tkinter import *
from tkinter import messagebox
from random import choice
from sample_text import sample_texts
import datetime as dt

TEXT_FONT = ('Arial', 14, 'bold')


def get_entry(var, index, mode):
    global entry, entered_word, words_to_type, words_num, test_started, start_time, end_time

    if not test_started:
        start_time = dt.datetime.now()
        test_started = True

    if entered_word.get() != "" and entered_word.get()[-1] == " ":
        if len(words_to_type) > 0:
            if entered_word.get()[:-1] == words_to_type[0]:
                words_to_type.pop(0)
                entry.delete(0, END)

                # Last element was removed end the test
                if len(words_to_type) == 0:
                    end_time = dt.datetime.now()

                    # Calculate test result
                    typing_speed = words_num / ((end_time - start_time).total_seconds() / 60)

                    messagebox.showinfo(title="Test result",
                                        message=f"Your typing speed is: {round(typing_speed, 2)} WPM")
                    window.destroy()


# Global variables needed to control the test
test_started = False
start_time = 0
end_time = 0

# Window configuration
window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20, background="#579BB1")

# Variable that triggers callback on every key inserted in entry
entered_word = StringVar()
entered_word.trace_add('write', get_entry)

# Prepare words to type and validate variables
training_text = choice(sample_texts)
words_to_type = training_text.split(' ')
words_num = len(words_to_type)

# Canvas
canvas = Canvas(width=300, height=150, bg="#F8F4EA")
canvas.grid(row=0, column=0)
text = canvas.create_text(150, 75, text=training_text, width=280, justify=CENTER, font=TEXT_FONT)

# Entry
entry = Entry(window, width=20, textvariable=entered_word, font=('Arial', 10, 'normal'))
entry.grid(row=1, column=0, pady=10)

window.mainloop()
