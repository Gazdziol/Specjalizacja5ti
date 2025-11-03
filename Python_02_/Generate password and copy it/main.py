from tkinter import *
from tkinter import messagebox
import random
import json

#Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    pass_entry.insert("a",password)



#--------------save password--------------------

def save():
    website = website_entry.get()
    email = email_entry.get()
    passw = pass_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": passw,
        }
    }

    if website == "":
        messagebox.showinfo(title="", message="You don't have website")
    elif email == "":
        messagebox.showinfo(title="", message="You don't have email")
    elif passw == "":
        messagebox.showinfo(title="", message="You don't have password")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {passw} \nIs it okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except (FileNotFoundError, json.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0,END)

#--------------find password-----------

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n"
                                                       f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")

#-----------------main---------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200,height=200)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image_logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

button_search = Button(text="Search", command=search, width=13)
button_search.grid(row=1, column=2)


email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dawidgazda17@gmail.com")

pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", command=save, width=36)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()