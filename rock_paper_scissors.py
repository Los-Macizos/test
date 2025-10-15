import random

def play():
    choices = ['rock', 'paper', 'scissors']
    print("\nRock Paper Scissors Game!")
    
    player = input("Choose (rock/paper/scissors): ").lower()
    computer = random.choice(choices)

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}\n")

    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    # Preguntar si quiere volver a jugar
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again == 'yes':
        play()  # 👈 vuelve a llamar la función y repite el juego
    else:
        print("Thanks for playing! 👋")

# Iniciar el juego
play()
