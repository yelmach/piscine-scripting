def clean_list(list):
    if not list:
        return list
    
    cleaned = [item.strip().capitalize() for item in list]
    
    if "Milk" not in cleaned:
        cleaned.append("Milk")
    
    return [f"{i}/ {item}" for i, item in enumerate(cleaned, start=1)]
