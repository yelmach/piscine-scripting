import json

class User:
    username = 'user'
    email = 'something@mail.com'

def create_new_user(json_string):
    data = json.loads(json_string)
    
    if "username" in data and "email" in data:
        new_user = User()
        new_user.username = data["username"]
        new_user.email = data["email"]
        return new_user
    
    return User()
    
def user_to_json(user_obj):
    user_dict = {
        "username": user_obj.username,
        "email": user_obj.email
    }
    
    return json.dumps(user_dict)