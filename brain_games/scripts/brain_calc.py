from brain_games.game_logic import (
    play_game, welcome_player, get_player_name, congratulate_player
)
from brain_games.games.game_calc import brain_calc_game_logic


def main():
    welcome_player()
    name = get_player_name()
    print("What is the result of the expression?")
    if play_game(brain_calc_game_logic):
        congratulate_player(name)


if __name__ == "__main__":
    main()
