from brain_games.game_logic import welcome_player, play_game
from brain_games.games.game_calc import task, game_calc_logic


def main():
    name = welcome_player()
    task()
    play_game(game_calc_logic, name)


if __name__ == "__main__":
    main()
