from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

# Colors definitions
BG_COLOR = "#E1D7C6"

image_path = None


def upload_file():
    global image_path

    image_file = filedialog.askopenfile()
    if image_file is not None:
        image_path = image_file.name
        canvas.itemconfig(image_name_text, text=image_path.split('/')[-1])
    else:
        image_path = None
        canvas.itemconfig(image_name_text, text='No image chosen')


def add_watermark():
    global image_path

    if image_path is None:
        messagebox.showerror(title="Error", message="No file specified!")
    else:
        image_path = None
        canvas.itemconfig(image_name_text, text='No image chosen')
        messagebox.showinfo(title="Info", message="Ok")


# UI setup
window = Tk()
window.title("Image Watermarker")
window.config(padx=20, pady=20, bg=BG_COLOR)

# Canvas
canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
image_name_text = canvas.create_text(100, 100, text='No image chosen')

# Buttons
upload_button_img = PhotoImage(file="images/add_image.png")
upload_button = Button(image=upload_button_img, highlightthickness=0, background=BG_COLOR, command=upload_file)
upload_button.grid(row=1, column=0)

process_button_img = PhotoImage(file="images/process_image.png")
process_button = Button(image=process_button_img, highlightthickness=0, background=BG_COLOR, command=add_watermark)
process_button.grid(row=1, column=1)

window.mainloop()
