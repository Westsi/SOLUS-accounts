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
import json
import absolute_url
import passlib.hash
import tkinter as tk


def get_user(username, password):
    # absolute url is complete url, secret for privacy reasons. C:/user/...
    file_of_user = absolute_url.absolute_url + username.lower() + '.json'
    print(file_of_user)
    f = open(file_of_user, 'r')
    fou = f.read()
    print(fou)
    user_info = json.loads(str(fou))
    print(user_info)
    if passlib.hash.sha512_crypt.verify(password, user_info['Pass']):
        print("Successfully logged in!")
    else:
        print("An error occured or password incorrect. Sorry about that! Please try again!")


def get_tk_input():
    ulurl = absolute_url.ul_absolute
    user_list = open(ulurl, 'r')
    users = user_list.readlines()
    print(users)
    user_list.close()
    username_input = str(username.get(1.0, "end-1c"))
    password_input = password.get(1.0, "end-1c")
    if username_input + '\n' in users:
        get_user(username_input.lower(), password_input)
    else:
        print("Make an account first!")


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

signup_button = tk.Button(window, text="Log in to the SOLUS!", command=get_tk_input)
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
