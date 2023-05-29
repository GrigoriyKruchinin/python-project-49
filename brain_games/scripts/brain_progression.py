from brain_games.game_logic import play_game
from brain_games.games.game_progression import TASK, game_progression_logic


def main():
    play_game(TASK, game_progression_logic)


if __name__ == "__main__":
    main()
