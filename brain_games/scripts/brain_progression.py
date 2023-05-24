from brain_games.game_logic import (
    play_game, welcome_player, get_player_name, congratulate_player, game_over
)
from brain_games.games.game_progression import brain_progression_game_logic


def main():
    welcome_player()
    name = get_player_name()
    print("What number is missing in the progression?")
    if play_game(brain_progression_game_logic):
        congratulate_player(name)
    else:
        game_over(name)


if __name__ == "__main__":
    main()
