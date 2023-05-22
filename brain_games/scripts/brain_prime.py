from brain_games.cli import welcome_user
from brain_games.logic_prime import play_prime_game


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')
    play_prime_game(name)


if __name__ == "__main__":
    main()
