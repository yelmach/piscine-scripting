import json

class User:
    username = 'user'
    email = 'something@mail.com'

def create_new_user(json_string):
    data = json.loads(json_string)
    
    new_user = User()
    
    new_user.username = data.get("username")
    new_user.email = data.get("email")
    
    return new_user
    
def user_to_json(user_obj):
    if user_obj.username is None and user_obj.email is None:
        return json.dumps({})
    
    user_dict = {
        "username": user_obj.username,
        "email": user_obj.email
    }
    
    return json.dumps(user_dict)
