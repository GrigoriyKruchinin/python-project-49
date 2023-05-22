from brain_games.cli import welcome_user
from brain_games.logic_gcd import play_gcd_game


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    play_gcd_game(name)


if __name__ == "__main__":
    main()
