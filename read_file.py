import json

def get_recipes(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        return data

recipes = get_recipes("recipes_data.json")
print(recipes)