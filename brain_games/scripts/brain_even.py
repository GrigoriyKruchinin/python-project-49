from brain_games.game_logic import (
    play_game, welcome_player, get_player_name, congratulate_player
)
from brain_games.games.game_even import brain_even_game_logic


def main():
    welcome_player()
    name = get_player_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if play_game(brain_even_game_logic):
        congratulate_player(name)


if __name__ == "__main__":
    main()
