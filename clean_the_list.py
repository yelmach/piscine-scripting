def clean_list(list):
    if not list:
        return list
    
    if 'milk' not in list:
        list.append('milk')
    
    return [f"{i}/ {item.strip().capitalize()}" for i, item in enumerate(list, start=1)]  
