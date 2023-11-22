import sys, time
print("|=====================================|",
      "\n|=== Day 3: Conditional Statements ===|",
      "\n|======= Programmed by: Vince ========|",
      "\n|=====================================|")

def printDial(txt, delay = 0.05):
    for x in txt:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(delay)
    print

printDial("\nYou find yourself stuck in the forest. There are multiple ways to get out but there are also path that will lead you to death!")
printDial("\nTry your best to get out of the forest. Goodluck!")
time.sleep(0.5)

printDial("\n\nThere are three paths: ")
printDial("\na.) Path with a bit of shoe print")
printDial("\nb.) Path with tire tracks")
printDial("\nc.) Path with no prints at all")

choice1 = input("\nWhich path would you take? (a/b/c): ")

if choice1 == "A" or choice1 == "a":
    printDial("\n\nAfter walking for a while, you find two paths: ")
    printDial("\na.) Path with cut-down logs")
    printDial("\nb.) Unnoticable small path with bike tracks")

    choice2 = input("\nWhich path would you take? (a/b): ")
    if choice2 == "A" or choice2 == "a":
        printDial("\n\nYou managed to pass through the logs but furious animals were behind the logs.")
        printDial("\nNice try!")
    elif choice2 == "B" or choice2 == "b":
        printDial("\n\nYou walked right through the small path and turned left.")
        printDial("\nYou noticed that it was full of tire tracks.")
        printDial("\nWell done! It was a long walk but you managed to get out of the forest!")
    else:
        print("\nINVALID INPUT. PROGRAM ENDED.")
elif choice1 == "B" or choice1 == "b":
    printDial("\n\nYou walked for miles, and it seemed that it was never going to end...")
    printDial("\nWell done! You almost gave up but since you didn't you manage to get out of the forest.")
elif choice1 == "C" or choice1 == "c":
    printDial("\n\nA fresh path with no tracks huh?")
    time.sleep(0.5)
    printDial("\nToo bad! You only got deeper into the forest and lost track of where you were going.")
else:
    print("\nINVALID INPUT. PROGRAM ENDED.")