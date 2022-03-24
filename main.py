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
import uuid
import json
import absolute_url
import passlib.hash
import tkinter as tk


def create_new_user(username, password):
    data = {'Username': username, 'Pass': password, 'UUID': str(uuid.uuid4()), 'Balance': 1000}
    print(data)
    ulurl = absolute_url.ul_absolute
    user_list_write = open(ulurl, 'a')
    try:
        # absolute url is complete url, secret for privacy reasons. C:/user/...
        file_for_storage = absolute_url.absolute_url + data['Username'].lower() + '.json'
        with open(file_for_storage, 'x') as file:
            json.dump(data, file)
        user_list_write.write(username.lower() + '\n')
    except FileExistsError:
        print("Username already taken. Please think of a new one!")
        taken_label.config(text="Username already taken. Please think of a new one!")

    user_list_write.close()


def cli_new_user():
    pref_username = input("Enter a username: \n")
    password = passlib.hash.sha512_crypt.hash(input("Password:\n"))

    create_new_user(pref_username.lower(), password)


def get_tk_input():
    username_input = str(username.get(1.0, "end-1c"))
    password_input = passlib.hash.sha512_crypt.hash(password.get(1.0, "end-1c"))
    create_new_user(username_input.lower(), password_input)


# user list
ulurl = absolute_url.ul_absolute
user_list = open(ulurl, 'r')
users = user_list.readlines()
print(users)
user_list.close()

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
