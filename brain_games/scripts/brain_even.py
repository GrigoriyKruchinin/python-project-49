from brain_games.game_logic import play_game
from brain_games.games.game_even import TASK, game_even_logic


def main():
    play_game(TASK, game_even_logic)


if __name__ == "__main__":
    main()
