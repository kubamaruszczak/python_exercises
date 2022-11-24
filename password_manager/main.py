from tkinter import *  # only import all classes, variables, funs etc. but no other module
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

FONT_NAME = "Courier"
BG_COLOR = "white"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = [choice(letters) for _ in range(randint(8, 10))]
    password += [choice(symbols) for _ in range(randint(2, 4))]
    password += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password)
    password = ''.join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # Copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get data from entries
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Ops", message="Don't leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                              f"Password: {password}\nIs it ok to save?")
        if is_ok:
            # Store data into the file
            with open(file="data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

            # Clear the entries and focus cursor on website entry
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BG_COLOR)
window.title("Password Manager")

# Image
canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg=BG_COLOR)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg=BG_COLOR)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=BG_COLOR)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # put the cursor in this entry

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "your@email.com")

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
