from brain_games.game_logic import play_game
from brain_games.games.game_calc import TASK, game_calc_logic


def main():
    play_game(TASK, game_calc_logic)


if __name__ == "__main__":
    main()
