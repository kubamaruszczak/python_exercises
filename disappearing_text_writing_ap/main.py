from tkinter import *

FONT = ("Arial", 10, "normal")

BG_COLORS = ["#FCFFE7", "#F8C4B4", "#E97777", "#DD5353", "#B73E3E"]

# Global variables
field_contents = ""
idle_time_cnt = 0


# Counting down and checking the text filed contents
def check_text():
    global text_field, field_contents, idle_time_cnt

    if field_contents != text_field.get("1.0", END):
        # Here you should reset the counter
        idle_time_cnt = 0
        field_contents = text_field.get("1.0", END)

    seconds_passed = idle_time_cnt // 10
    if seconds_passed == 5:
        # Time has elapsed so reset the timers
        seconds_passed = 0
        idle_time_cnt = 0
        # Delete Text entry contents
        text_field.delete("1.0", END)

    # Control the background color
    window.config(bg=BG_COLORS[seconds_passed])

    # If text field is not empty increment the timer
    if field_contents != "\n":
        idle_time_cnt += 1
    window.after(100, check_text)


# UI Setup
window = Tk()
window.title("The Most Dangerous Writing App")
window.config(padx=20, pady=20, bg=BG_COLORS[0])

# Text field configuration
text_field = Text(font=FONT, width=60, height=20)
text_field.grid(row=0, column=0)
text_field.focus()

# Scrollbar configuration
scrollbar = Scrollbar(window, orient="vertical", command=text_field.yview)
scrollbar.grid(row=0, column=1, sticky="nsew")
text_field.configure(yscrollcommand=scrollbar.set)

# Begin the check text box procedure
window.after(100, check_text)

window.mainloop()
