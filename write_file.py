def to_do(tasks):
    with open("output.txt", "w") as file:
        for task in tasks:
            formatted_date = task[0].strftime("%A %d %B %Y")
            file.write(f"{formatted_date}: {task[1]}\n")
