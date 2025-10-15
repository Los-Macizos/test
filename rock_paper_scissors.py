import random

choices = ['rock', 'paper', 'scissors']

print("Rock Paper Scissors Game!")

# Bucle principal del juego
while True:
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
    if again != 'yes':
        print("Thanks for playing! 👋")
        break
