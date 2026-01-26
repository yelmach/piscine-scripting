def clean_list(list):
    if not list:
        return list
    
    if "milk" not in list:
        list.append("milk")
    
    formatted_list = []
    
    for i, item in enumerate(list, start=1):
        formatted_list.append(f"{i}/ {item.strip().capitalize()}")
        
    return formatted_list
