#Password Generator
import random
from tkinter import *
from tkinter import messagebox
import pyperclip

FONT = "Arial"
fs = 12

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    input_pass.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    email = input_username.get()
    password = input_pass.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        ok_save = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        if ok_save:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                input_website.delete(0, 'end')
                input_pass.delete(0, 'end')
                input_website.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")
# app_width = 600
# app_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# x = (screen_width / 2) - (app_width / 2)
# y = (screen_height / 2) - (app_height / 2)
# window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_username = Label(text="Email/Username:")
label_username.grid(row=2, column=0)
label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

input_website = Entry(width=51)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()
input_username = Entry(width=51)
input_username.grid(row=2, column=1, columnspan=2)
input_username.insert(0, "ruffaresentes@gmail.com")
input_pass = Entry(width=33)
input_pass.grid(row=3, column=1)
button_generate = Button(text="Generate Password", highlightthickness=0, command=generate)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=43, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
