from random import choice

from .game import check_win


ROCK_PAPER_SCISSORS = {
    "rock": {"scissors"},
    "paper": {"rock"},
    "scissors": {"paper"},
}

if __name__ == "__main__":
    options = ROCK_PAPER_SCISSORS
    user_selection = input(f"Please choose one of: {options.keys()}\n")
    computer_selection = choice(list(options.keys()))
    print(f"Computer chose {computer_selection}")
    user_won = check_win(user_selection, computer_selection, options)
    if user_won:
        print("You won!")
    else:
        print("You lost!")
