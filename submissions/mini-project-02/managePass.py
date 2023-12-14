import json, os

def options():
    optionList = ["1. Add a Password, Email, and Name of Website",
                  "2. View all item",
                  "3. Search an item",
                  "4. Delete an item",
                  "5. Update an item",
                  "6. Exit"]
    return optionList

def check_webExist(webName):
    fileName = 'submissions\mini-project-02\dbPass.json'
    with open(fileName, 'r') as file:
        data = json.load(file)
        if webName not in data:
            print("Website does not exist.\n")
            return False
        else:
            return True
        

def add():
    website = input("Enter website name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    new_data = {
        website: [{
            'email': email,
            'password': password
        }]
    }
 
    fileName = 'submissions\mini-project-02\dbPass.json'
    with open(fileName, 'r') as file:
        data = json.load(file)

    if website not in data:
        data.update(new_data)
    else:
        data[website].append({'email': email, 'password': password})

    with open(fileName, 'w') as file:
        json.dump(data, file, indent=4)

    os.system('cls')
    print("Successfully added!")

def view():
    fileName = 'submissions\mini-project-02\dbPass.json'
    with open(fileName, 'r') as file:
        data = json.load(file)
        for name, val in data.items():
            print(f"Website: {name}")
            for x in range(len(val)):
                print(f"\tEmail: {val[x]['email']}")
                print(f"\tPassword: {val[x]['password']}")

def search(webName):
    fileName = 'submissions\mini-project-02\dbPass.json'
    with open(fileName, 'r') as file:
        data = json.load(file)
        for name, val in data.items():
            if name == webName:
                print(f"Website: {name}")
                for x in range(len(val)):
                    print(f"\t{x+1}. Email: {val[x]['email']}")
                    print(f"\t   Password: {val[x]['password']}")
                return True
            
        print("Website does not exist.")
            
def delete(webName):
    fileName = 'submissions\mini-project-02\dbPass.json'
    with open(fileName, 'r') as file:
        data = json.load(file)
        search(webName)

        item = int(input("Enter the NUMBER of the ITEM you want to DELETE: "))
        if 0 <= item-1 < len(data[webName]):
            data[webName].pop(item-1)
            with open(fileName, 'w') as file:
                json.dump(data, file, indent=4)

                print("Successfully removed.")
            if len(data[webName]) == 0:
                data.pop(webName)
                with open(fileName, 'w') as file:
                    json.dump(data, file, indent=4)

                    print("Website is empty. Website removed.")
        else:
            print("Error. Invalid input.")
            return

def update(webName):
    fileName = 'submissions\mini-project-02\dbPass.json'
    with open(fileName, 'r') as file:
        data = json.load(file)
        search(webName)

        item = int(input("Enter the NUMBER of the ITEM you want to UPDATE: "))
        if 0 <= item-1 < len(data[webName]):
            updateItem = input("What would you like to update? Email or Password: ").lower()
            newValue = input(f"Enter your new {updateItem}: ")
            data[webName][item-1][updateItem] = newValue
            with open(fileName, 'w') as file:
                json.dump(data, file, indent=4)

                print("Update successful.")
        else:
            print("Error. Invalid input.")
            return

