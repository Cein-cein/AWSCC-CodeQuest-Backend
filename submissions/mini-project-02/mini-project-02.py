import managePass

print("|===============================================|",
      "\n|=== Day 15: Mini Project (Password Manager) ===|",
      "\n|============ Programmed  by: Vince ============|",
      "\n|===============================================|")

menu = managePass.options()

print("\nWelcome to Password Manager! What's your agenda today?\n")

manage = True
while manage:
    for lines in menu:
        print(lines.strip())

    user = int(input("Enter choice: "))
    print("")
    if user == 1:
        managePass.add()
    elif user == 2:
        managePass.view()
        print("")
    elif user == 3:
        web = input("Enter website name: ")
        managePass.search(web)
    elif user == 4:
        web = input("Enter website name: ")
        managePass.delete(web)
    elif user == 5:
        exist = False
        while not exist:
            web = input("Enter website name: ")
            exist = managePass.check_webExist(web)
        managePass.update(web)
    elif user == 6:
        manage = False
    else:
        print("Invalid input.")
        manage = False