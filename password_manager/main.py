from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

EMAIL = "sonyakondratskaya@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "username": username,
        "password": password
    }}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning("Oops!", "You didn't enter some fields")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"These are the details entered for {website}\n\n"
                                                 f" Username: {username}\n"
                                                 f"Password: {password}\n\n"
                                                 f"Is it okay to save?",
                                         )
        if is_okay:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- GET WEBSITE DETAILS ------------------------------- #


def search_for_website():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Oops!", "File does not exist.")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("Oops!", "Something went wrong.")
    else:
        if website in data:
            website_details = data[website]
            messagebox.showinfo(website, f"Details for {website}\n\n"
                                         f"Username: {website_details['username']}\n"
                                         f"Password: {website_details['password']}\n")
        else:
            messagebox.showinfo(website, f"No details for {website}\n")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=20)

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(window, width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(window, text="Website")
website_label.grid(column=0, row=1)

username_label = Label(window, text="Email/Username")
username_label.grid(column=0, row=2)

password_label = Label(window, text="Password")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

username_entry = Entry(width=35)
username_entry.insert(0, EMAIL)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
password_gen_button = Button(window, text="Generate", command=generate_password, width=10)
password_gen_button.grid(column=2, row=3)

save_button = Button(window, text="Save Password", command=save_data, width=33)
save_button.grid(column=1, row=4, columnspan=2)

search_button = Button(window, text="Search", command=search_for_website, width=10)
search_button.grid(column=2, row=1)

window.mainloop()
