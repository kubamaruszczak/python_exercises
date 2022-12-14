from tkinter import *  # only import all classes, variables, funs etc. but no other module
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Ops", message="Don't leave any of the fields empty!")
    else:
        # Read actually existing data with error handling
        try:
            with open(file="data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
                # Updating data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        # Update data with new record or create a file if file doesn't exist
        with open(file="data.json", mode="w") as file:
            # Saving updated data
            json.dump(data, file, indent=4)

        # Clear the entries and focus cursor on website entry
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for given website exists.")


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
website_entry = Entry(width=27)
website_entry.grid(row=1, column=1, sticky="W", padx=5)
website_entry.focus()  # put the cursor in this entry

email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W", padx=5)
email_entry.insert(0, "your@email.com")

password_entry = Entry(width=27)
password_entry.grid(row=3, column=1, sticky="W", padx=5)

# Buttons
generate_button = Button(text="Generate", width=5, command=generate_password)
generate_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=5, command=search)
search_button.grid(row=1, column=2, sticky="W")

window.mainloop()
