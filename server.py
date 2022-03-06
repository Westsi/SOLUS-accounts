# imports
import uuid
import json
import absolute_url
# from client import taken_label


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
        print("User created!")
    except FileExistsError:
        print("Username already taken. Please think of a new one!")
        # taken_label.config(text="Username already taken. Please think of a new one!")

    user_list_write.close()
