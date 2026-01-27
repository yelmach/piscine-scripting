import json
import os

def find_keys(data, found_credentials):
    if isinstance(data, dict):
        for key, value in data.items():
            if key in ["password", "secret"]:
                found_credentials[key] = value
            elif isinstance(value, (dict, list)):
                find_keys(value, found_credentials)
                
    elif isinstance(data, list):
        for item in data:
            find_keys(item, found_credentials)

def credentials_search():
    filename = "logs.json"
    
    if not os.path.exists(filename):
        return

    try:
        with open(filename, 'r') as file:
            content = file.read()
            if not content.strip():
                return
            data = json.loads(content)
    except (json.JSONDecodeError, IOError):
        return

    found_credentials = {}
    find_keys(data, found_credentials)

    if found_credentials:
        with open("credentials.json", "w") as outfile:
            json.dump(found_credentials, outfile)

if __name__ == "__main__":
    credentials_search()