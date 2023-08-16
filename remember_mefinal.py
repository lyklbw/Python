import json
def get_storage():
    file_name="username.json"
    try:
        with open(file_name) as file:
            content=json.load(file)
    except FileNotFoundError:
        return None
    else:
        return content
    
def get_new_storage():
    username=input("What is your name?")
    file_name="username.json"
    with open(file_name,"w") as file:
        json.dump(username,file)
    return username

def greet_user():
    username=get_storage()
    if username:
        print("Welcome back "+username)
    else:
        username=get_new_storage()
        print("We will remember you when you come back "+username)

greet_user()