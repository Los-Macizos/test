import random

def play():
    contador_player = 0
    contador_computer = 0
    contador_tie = 0

    while True:
        if contador_tie > 2:
            print(f"\nMore than three ties — nobody wins. ({contador_tie} ties)")
            break
        elif contador_player > 2 and contador_player > contador_computer:
            print(f"\nFinal Score → Player: {contador_player}, Computer: {contador_computer}")
            print("🎉 Player wins the match!")
            break
        elif contador_computer > 2 and contador_computer > contador_player:
            print(f"\nFinal Score → Player: {contador_player}, Computer: {contador_computer}")
            print("💻 Computer wins the match!")
            break
        else:
            choices = ['rock', 'paper', 'scissors']

            print("\nRock Paper Scissors Game!")
            player = input("Choose (rock/paper/scissors): ").lower()
            computer = random.choice(choices)

            print(f"\nYou chose: {player}")
            print(f"Computer chose: {computer}\n")

            if player == computer:
                print("It's a tie!")
                contador_tie += 1
            elif (player == 'rock' and computer == 'scissors') or \
                 (player == 'paper' and computer == 'rock') or \
                 (player == 'scissors' and computer == 'paper'):
                print("You win this round!")
                contador_player += 1
            else:
                print("Computer wins this round!")
                contador_computer += 1

    # Preguntar si quiere volver a jugar
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again == 'yes':
        play()
    else:
        print("Thanks for playing! 👋")

# Iniciar el juego
play()
