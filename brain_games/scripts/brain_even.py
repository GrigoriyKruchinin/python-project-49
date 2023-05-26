from brain_games.game_logic import welcome_player, play_game
from brain_games.games.game_even import task, game_even_logic


def main():
    name = welcome_player()
    task()
    play_game(game_even_logic, name)


if __name__ == "__main__":
    main()
