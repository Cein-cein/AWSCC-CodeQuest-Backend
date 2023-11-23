print("|================================|",
      "\n|=== Day 4: Logical Operators ===|",
      "\n|===== Programmed by: Vince =====|",
      "\n|================================|",)

print("\nRock, Paper, Scissors Game!")



while True:
    player1 = input("\nPlayer 1: ")
    player2 = input("Player 2: ")

    #Player 1 wins
    if player1.lower() == "rock" and player2.lower() == "scissors":
        print("\nPLAYER 1 WINS!!!")
    elif player1.lower() == "paper" and player2.lower() == "rock":
        print("\nPLAYER 1 WINS!!!")
    elif player1.lower() == "scissors" and player2.lower() == "paper":
        print("\nPLAYER 1 WINS!!!")

    #Player 2 wins
    elif player2.lower() == "rock" and player1.lower() == "scissors":
        print("\nPLAYER 2 WINS!!!")
    elif player2.lower() == "paper" and player1.lower() == "rock":
        print("\nPLAYER 2 WINS!!!")
    elif player2.lower() == "scissors" and player1.lower() == "paper":
        print("\nPLAYER 2 WINS!!!")

    #Draw
    elif player1.lower() == "rock" and player2.lower() == "rock":
        print("\nDRAW!!!")
    elif player1.lower() == "paper" and player2.lower() == "paper":
        print("\nDRAW!!!")
    elif player1.lower() == "scissors" and player2.lower() == "scissors":
        print("\nDRAW!!!")
    else:
        print("\nINVALID INPUT. PROGRAM ENDED.")

    #Asks players if they want to play again
    playAgain = input("\nDo you want to play again? (Yes/No): ")
    if playAgain.lower() == "yes":
        True
    elif playAgain.lower() == "no":
        print("\nThank you for playing!")
        break
    else:
        print("\nINVALID INPUT. PROGRAM ENDED")
