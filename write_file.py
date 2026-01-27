def to_do(tasks):
    for task in tasks:
        formatted_date = task[0].strftime("%A %d %B %Y")
    
        with open("output.txt", "a") as file:
            file.write(f"{formatted_date}: {task[1]}\n")
