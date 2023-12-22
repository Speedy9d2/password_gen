from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers

    shuffle(password_list)

    final_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website = website_text_entry.get()
    login = login_info_entry.get()
    user_password = password_entry.get()

    new_data = {
        website: {
            "email": login,
            "password": user_password,
        }
    }

    if len(website) == 0 or len(login) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Missing Information", message="Please do not leave any fields blank")
    else:
        try:
            with open("User_Information.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("User_Information.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("User_Information.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_text_entry.delete(0, END)
            login_info_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- WEBSITE SEARCH ------------------------------- #

def find_password():
    website = website_text_entry.get().title()
    try:
        with open("User_Information.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox.showinfo(title="Login information", message=f"Email: {data[website]["email"]}\n "
                                                                       f"Password: {data[website]["password"]}")
    except FileNotFoundError:
        messagebox.showinfo(title="Missing File", message="There's no file to be accessed")


# ---------------------------- UI SETUP ------------------------------- #

# Window UI
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20, bg="white")

# Canvas UI
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# User Input UI
website_text = Label(text="Website:", fg="black", bg="white")
website_text.grid(row=1, column=0)

# Website Entry
website_text_entry = Entry(width=21, fg="black", bg="white", highlightthickness=0)
website_text_entry.grid(row=1, column=1)
website_text_entry.focus()

login_info = Label(text="Email/Login:", fg="black", bg="white")
login_info.grid(row=2, column=0)

# Login Entry
login_info_entry = Entry(width=35, fg="black", bg="white", highlightthickness=0)
login_info_entry.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:", fg="black", bg="white")
password.grid(row=3, column=0)

# Password Entry
password_entry = Entry(width=21, fg="black", bg="white", highlightthickness=0)
password_entry.grid(row=3, column=1)

# Buttons
add_button = Button(width=32, text="Add", bg="white", bd=0, highlightthickness=0, command=save_info)
add_button.grid(row=4, column=1, columnspan=2)
generate_password = Button(text="Generate Password", bg="white", bd=0,
                           highlightthickness=0, width=10, command=password_gen)
generate_password.grid(row=3, column=2)
search_button = Button(width=10, text="Search", bg="white", bd=0, highlightthickness=0, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
