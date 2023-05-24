from brain_games.game_logic import (
    play_game, welcome_player, get_player_name, congratulate_player, game_over
)
from brain_games.games.game_gcd import brain_gcd_game_logic


def main():
    welcome_player()
    name = get_player_name()
    print("Find the greatest common divisor of given numbers.")
    if play_game(brain_gcd_game_logic):
        congratulate_player(name)
    else:
        game_over(name)


if __name__ == "__main__":
    main()
