from brain_games.game_logic import play_game
from brain_games.games.game_gcd import TASK, game_gcd_logic


def main():
    play_game(TASK, game_gcd_logic)


if __name__ == "__main__":
    main()
