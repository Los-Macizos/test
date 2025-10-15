import random

choices = ['rock', 'paper', 'scissors']

print("Rock Paper Scissors Game!")
player = input("Choose (rock/paper/scissors): ").lower()
computer = random.choice(choices)

print(f"You chose: {player}")
print(f"Computer chose: {computer}")

if player == computer:
    print("It's a tie!")
elif (player == 'rock' and computer == 'scissors') or \
     (player == 'paper' and computer == 'rock') or \
     (player == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("Computer wins!")
