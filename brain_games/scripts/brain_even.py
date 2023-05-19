from brain_games.cli import welcome_user
from brain_games.logic_even import play_game


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    play_game(name)


if __name__ == "__main__":
    main()
