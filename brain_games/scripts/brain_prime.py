from brain_games.game_logic import (
    play_game, welcome_player, get_player_name, congratulate_player, game_over
)
from brain_games.games.game_prime import brain_prime_game_logic


def main():
    welcome_player()
    name = get_player_name()
    print("Answer 'yes' if the number is prime, otherwise answer 'no'.")
    if play_game(brain_prime_game_logic):
        congratulate_player(name)
    else:
        game_over(name)


if __name__ == "__main__":
    main()
