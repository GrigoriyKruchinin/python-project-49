from brain_games.cli import welcome_user
from brain_games.logic_progression import play_progression_game


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What number is missing in the progression?")
    play_progression_game(name)


if __name__ == "__main__":
    main()
