from .game import check_win

ROCK_PAPER_SCISSORS = {
    "rock": {"scissors"},
    "paper": {"rock"},
    "scissors": {"paper"},
}

if __name__ == "__main__":
    options = ROCK_PAPER_SCISSORS
    selection = input(f"Please choose one of: {options.keys()}\n")
    computer_selection = choice(list(options.keys()))
    user_won = check_win(user_selection, computer_selection, options)
    if user_won:
        print("You won!")
    else:
        print("You lost!")
