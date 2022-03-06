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
    user_list_write = open('user_list.txt', 'a')
    try:
        # absolute url is complete url, secret for privacy reasons. C:/user/...
        file_for_storage = absolute_url.absolute_url + data['Username'].lower() + '.json'
        with open(file_for_storage, 'x') as file:
            json.dump(data, file)
        user_list_write.write(username.lower() + '\n')
    except FileExistsError:
        print("Username already taken. Please think of a new one!")
        cli_new_user()

    user_list_write.close()


def cli_new_user():
    pref_username = input("Enter a username: \n")
    password = passlib.hash.sha512_crypt.hash(input("Password:\n"))

    create_new_user(pref_username.lower(), password)


def get_tk_input():
    username_input = username.get(1.0, "end-1c")
    password_input = passlib.hash.sha512_crypt.hash(password.get(1.0, "end-1c"))
    create_new_user(username_input.lower, password_input)


# user list
user_list = open('user_list.txt', 'r')
users = user_list.readlines()
print(users)
user_list.close()

window = tk.Tk()
window.title("Welcome to the SOLUS")
window.geometry('400x200')
username_label = tk.Label(window, text="Username:")
username = tk.Text(window)
password_label = tk.Label(window, text="Password:")
password = tk.Text(window)

signup_button = tk.Button(window, text="Join the SOLUS!", command=get_tk_input)
# cli_new_user()
