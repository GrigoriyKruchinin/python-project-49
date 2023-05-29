from brain_games.game_logic import play_game
from brain_games.games.game_prime import TASK, game_prime_logic


def main():
    play_game(TASK, game_prime_logic)


if __name__ == "__main__":
    main()
