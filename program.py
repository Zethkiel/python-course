import random

rps = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(rps)

def get_human_choice():
    return input("Rock, paper, or scissors?\n")

human_score = 0
computer_score = 0

def play_round(human_choice, computer_choice):
    global no_input, invalid_input
    no_input = "There was no input."
    invalid_input = "Invalid input!"
    tie = "It's a tie!"

    if not human_choice:
        return no_input
    elif human_choice not in rps:
        return invalid_input
    elif human_choice == computer_choice:
        return tie
        
    result =  {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    global human_score, computer_score

    if result[human_choice] == computer_choice:
        human_score += 1
        return f"You win! {human_choice.capitalize()} beats {computer_choice.capitalize()}"
    else:
        computer_score += 1
        return f"You lose! {computer_choice.capitalize()} beats {human_choice.capitalize()}"

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