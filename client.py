"""
To store in jsons
Username
Hashed password
UUID- why?!
bank balance
character
date account made
email address
"""

# imports
import passlib.hash
import tkinter as tk
from server import create_new_user


def get_tk_input():
    username_input = str(username.get(1.0, "end-1c"))
    password_input = passlib.hash.sha512_crypt.hash(password.get(1.0, "end-1c"))
    create_new_user(username_input.lower(), password_input)


window = tk.Tk()
window.title("Welcome to the SOLUS")
window.geometry('400x200')
username_label = tk.Label(window, text="Username:")
username_label.place(x=80, y=100)
username = tk.Text(window, height=5, width=20)
username.place(x=80, y=120)
password_label = tk.Label(window, text="Password:")
password_label.place(x=80, y=140)
password = tk.Text(window, height=5, width=20)
password.place(x=80, y=160)

signup_button = tk.Button(window, text="Join the SOLUS!", command=get_tk_input)
signup_button.place(x=80, y=180)

taken_label = tk.Label(window, text="")
taken_label.place(x=80, y=200)

# packing everything
username_label.pack()
username.pack()
password_label.pack()
password.pack()
signup_button.pack()
taken_label.pack()

tk.mainloop()
