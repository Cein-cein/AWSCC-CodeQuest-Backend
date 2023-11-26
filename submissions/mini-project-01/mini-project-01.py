print("\t\t\t\t|==============================================|",
      "\n\t\t\t\t|=== Day 7: Mini Project 01 (Shopping List) ===|",
      "\n\t\t\t\t|=========== Programmed by : Vince ============|",
      "\n\t\t\t\t|==============================================|")

print("\n\t\t\t   Welcome to your very own shopping list! Have fun shopping!")

#Create variable with empty list
shopList = []

#Create and set variable quit to false
Quit = False

#Loop until quit is true
while not Quit:
    print("\n\t\t\t   Options: ",
      "\n\t\t\t   1. Add item to the shopping list",
      "\n\t\t\t   2. View shopping list",
      "\n\t\t\t   3. Remove item from the shopping list",
      "\n\t\t\t   4. Quit")
    
    userChoice = int(input("\t\t\t   Enter the number of your choice: "))

    if userChoice == 1:
        shopItem = input("\t\t\t   Enter the item you want to add: ")
        #Adds inputted item to the empty list
        shopList.append(shopItem)
    elif userChoice == 2:
        print("\t\t\t   Your shopping list:")
        #Use for loop to access and print list
        #Use the length of list as the range
        for x in range(len(shopList)):
            print(f"\t\t\t   {shopList[x]}")
    elif userChoice == 3:
        removeItem = input("\t\t\t   Enter the item you want to remove: ")

        #Validates if item exist or spelled correctly
        if removeItem == shopItem:
            #Removes item from list
            shopList.remove(removeItem)
            print(f"\t\t\t   {removeItem} has been removed from your shopping list")
        else:
            print("\t\t\t   You must've misspelled the item or it does not exist.")
    elif userChoice == 4:
        #Set variable quit to true to break loop
        Quit = True
        print("\t\t\t   I hope you enjoyed shopping today! Goodbye!")
    else:
        print("\t\t\t   INVALID INPUT. PLEASE TRY AGAIN.")
