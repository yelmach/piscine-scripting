day_map = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday",
}

def day_from_number(day_number):    
    return day_map.get(day_number)

def day_to_number(day):
    for k, v in day_map.items():
        if v == day:
            return k
    return None
