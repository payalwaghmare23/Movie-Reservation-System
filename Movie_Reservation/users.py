users = {}

def signup(username , password , city):
    if username in users :
        return "User already exists."
    
    else :
        users[username] = {
        "password" : password , 
        "city" : city 
        }
        return "SingUp Successful."


def login(username , password):
    if username in users and users[username]["password"] == password:
        return True
    return False

def get_user_city(username):
    return users[username]["city"]