from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_numbers

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
    # messagebox.showinfo("Password Generated", "Password has been copied to clipboard")
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill all fields")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH DETAILS ------------------------------- #
def search():
    website = website_entry.get()

    if len(website) != 0:
        try:
            with open("data.json", "r") as file:
                json_data = json.load(file)

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="file not found")

        else:
            if website in json_data:
                password = json_data[website]["password"]
                email = json_data[website][ "email"]

                messagebox.showinfo(title=website, message=f"Your password is: {password}\n"
                                                            f"Your email is: {email}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exist")


    else:
        messagebox.showerror(title="Error", message="field cannot be empty")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


# entries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "hujjatullarh@gmail.com")


password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

# buttons
gen_pass = Button(text="Generate Password", width=18, command=generate_password)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save_details)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search",width=13, command=search)
search_button.grid(row=1, column=2)



window.mainloop()