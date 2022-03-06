import tkinter as tk
import passlib.hash
from main import create_new_user


def get_tk_input():
    username_input = username.get(1.0, "end-1c")
    password_input = passlib.hash.sha512_crypt.hash(password.get(1.0, "end-1c"))
    create_new_user(username_input.lower, password_input)


window = tk.Tk()
window.title("Welcome to the SOLUS")
username_label = tk.Label(window, text="Username:")
username = tk.Text(window)
password_label = tk.Label(window, text="Password:")
password = tk.Text(window)

signup_button = tk.Button(window, text="Join the SOLUS!", command=get_tk_input)
