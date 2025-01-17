# Rock Paper Scissors Project
import random

while True:
    move = input("Rock Paper or Scissors? ")
    if move.lower() != "rock" and move.lower() != "paper" and move.lower() != "scissors":
        print("Please choose a correct answer")
        continue
    moveC = random.choice(["Rock", "Paper", "Scissors"])
    print("Computer chose ", moveC)

    if move.lower() == moveC.lower():
        print(f"Both players selected {move.capitalize()}. It's a tie")
    elif move.lower() == "rock":
        if moveC.lower() == "scissors":
            print("Rock smashes Scissors. You win.")
        else:
            print("Paper covers Rock. You lose.")
    elif move.lower() == "paper":
        if moveC.lower() == "rock":
            print("Paper covers Rock. You win.")
        else:
            print("Scissors cut Paper. You lose.")
    elif move.lower() == "scissors":
        if moveC.lower() == "paper":
            print("Scissors cut Paper. You win.")
        else: 
            print("Rock smashes Scissors. You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
