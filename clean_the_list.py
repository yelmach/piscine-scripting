def clean_list(list):
    if not list:
        return list
    
    formatted = [item.strip().capitalize() for item in list]  
      
    if "Milk" not in list:
        list.append("Milk")
    
    return [f"{i}/ {item}" for i, item in enumerate(formatted, start=1)]  
