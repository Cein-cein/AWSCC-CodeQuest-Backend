import random
print("|============================|",
      "\n|=== Day 5: Randomization ===|",
      "\n|=== Programmed by: Vince ===|",
      "\n|============================|")

print("\nPlay rock, paper, scissors with a computer!")

while True:
    moveList = ["rock", "paper", "scissors"]
    computer = random.choice(moveList)

    user = input("\nEnter your move: ").lower()

    #User wins
    if user == "rock" and computer == "scissors":
        print("\nYou win! Congratulations!")
    elif user == "paper" and computer == "rock":
        print("\nYou win! Congratulations!")
    elif user == "scissors" and computer =="paper":
        print("\nYou win! Congratulations!")

    #Computer wins
    elif computer == "rock" and user == "scissors":
        print("\nYou lost! Better luck next time!")
    elif computer == "paper" and user == "rock":
        print("\nYou lost! Better luck next time!")
    elif computer == "scissors" and user == "paper":
        print("\nYou lost! Better luck next time!")

    #Draw
    elif user == "rock" and computer == "rock":
        print("\nDRAW!!!")
    elif user == "paper" and computer == "paper":
        print("\nDRAW!!!")
    elif user == "scissors" and computer == "scissors":
        print("\nDRAW!!!")
    else:
        print("\nINVALID INPUT. PROGRAM ENDED.")
        break

    playAgain = input("Do you want to play again? (Yes/No): ").lower()
    if playAgain == "yes":
        True
    elif playAgain == "no":
        print("\nThank you for playing. I hope you enjoyed the game!")
        break
    else:
        print("\nINVALID INPUT. PROGRAM ENDED.")
        break
