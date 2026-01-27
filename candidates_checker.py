import sys

def main():
    if len(sys.argv) != 2:
        print("Error: wrong number of arguments")
        sys.exit(1)
        
    candidates = []
    for i in range(int(sys.argv[1])):
        print("Add a new candidate:")
        name = input("name: ")
        age = int(input("age: "))
    
        condidate = {}
    
        if age < 18:
            condidate["message"] = f"{name} is not eligible (underaged)"
        elif age > 60:
            condidate["message"] = f"{name} is not eligible (over the legal age)"
        else:
            condidate["message"] = f"{name} is eligible"
    
        candidates.append(condidate)
    
    for person in candidates:
        print(person["message"])
    
if __name__ == "__main__":
    main()