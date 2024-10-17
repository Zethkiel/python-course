# Import a module that generates a random variable.
import random

rps = ["rock", "paper", "scissors"]

# Get a random choice from the computer.
def get_computer_choice():
    return random.choice(rps)

def get_human_choice():
    return input("Rock, paper, or scissors?\n")

# Pre-defining score variables. Each will be incremented depending on the winner of each round.
human_score = 0
computer_score = 0

# This function plays a single round of rock paper scissors.
def play_round(human_choice, computer_choice):
    global no_input, invalid_input
    no_input = "There was no input."
    invalid_input = "Invalid input!"
    tie = "It's a tie!"

    # Check if the user inputs an invalid choice.
    if not human_choice:
        return no_input
    elif human_choice not in rps:
        return invalid_input
    elif human_choice == computer_choice:
        return tie
    
    # This dictionary pre-defines the rules for the game. Each key-value pair shows which item defeats which
    # This helps cut down on messy and repeated if/else statements which determines the winner.
    result =  {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    # Required to modify variables outside of this function.
    global human_score, computer_score

    # Check if human_choice beats computer_choice as per the dictionary, then increment the scores.
    if result[human_choice] == computer_choice:
        human_score += 1
        return f"You win! {human_choice.capitalize()} beats {computer_choice.capitalize()}"
    else:
        computer_score += 1
        return f"You lose! {computer_choice.capitalize()} beats {human_choice.capitalize()}"

# This function will make the rounds loop 5 times, then print the winner by the end of the loop.
def play_game():
    i = 0
    while i < 5:
        human_selection = get_human_choice()
        computer_selection = get_computer_choice()
        result = play_round(human_selection, computer_selection)

        if result is not invalid_input and result is not no_input:
            i += 1
        print(result)

    print(f"Human: {human_score}, Computer: {computer_score}")

    if human_score > computer_score:
        print("Congrats! You won the game.")
    elif human_score < computer_score:
        print("You lost the game. Better luck next time!")
    else:
        print("It's an overall tie!")

play_game()