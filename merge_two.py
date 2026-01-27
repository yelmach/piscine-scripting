import json

def merge_two(first_dict):
    second_dict = {}
    while True:
        print("Add a new entry:")
        key = input("key: ")
        if key == "exit":
            break
        
        val = int(input("value: "))
        second_dict[key] = val
    
    res = first_dict | second_dict
    
    return json.dumps(res)
