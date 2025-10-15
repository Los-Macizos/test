import random

contador_player = 0
contador_computer = 0
contador_tie = 0

while True :
    if contador_tie > 2:
        print (f" More than three ties — nobody wins. {contador_tie}")
        break
    elif contador_player > 2 and contador_player > contador_computer:
        print( f"Player points: {contador_player} and Computer points: {contador_computer}")
        break
    elif contador_computer > 2 and contador_computer > contador_player :
        print( f"Player points: {contador_player} and Computer points: {contador_computer}")
        break
    else: 
        choices = ['rock', 'paper', 'scissors']

        print("Rock Paper Scissors Game!")
        player = input("Choose (rock/paper/scissors): ").lower()
        computer = random.choice(choices)

        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")
        if player == computer:
            print("It's a tie!")
            contador_tie += 1
        elif (player == 'rock' and computer == 'scissors') or \
            (player == 'paper' and computer == 'rock') or \
            (player == 'scissors' and computer == 'paper'):
            print("You win!")
            contador_player +=1
        
        else:
            print("Computer wins!")
            contador_computer +=1

