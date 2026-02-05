import random 


options = ("rock" ,"paper" , "scissors")



running = True

while running:
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Enter a choice (rock,  paper ,scissors): ")

    print(f"player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie")
    elif player == "rock" and computer == "scissors":
        print("You wins")
    elif player == "rock" and computer == "paper":
        print("You Lose")
    elif player == "scissors" and computer == "paper":
        print("You Wins")
    elif player == "scissors" and computer == "rock":
        print("You Lose")
    elif player == "paper" and computer == "rock":
        print("You Lose")
    elif player == "papar" and computer == "scissors":
        print("You Wins")
    play_again = input("do you like to play the game again (y/n) ?").lower()
    if play_again == "n":
        running = False
        
print("thanks for playing")