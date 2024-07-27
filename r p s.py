import random

#This line imports the random module, which allows us to generate random choices for the computer.
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

#This function gets the computer choice
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

#This function gets user choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:  
        return "Computer wins!"
    
#This function Get both choice from user and computer and Declare Winner
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

# Main Part of game
print("Welcome to Rock, Paper, Scissors!")
play_game()
