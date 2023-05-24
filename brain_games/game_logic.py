import prompt


def welcome_player():
    print("Welcome to the Brain Games!")


def get_player_name():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def congratulate_player(name):
    print(f"Congratulations, {name}!")


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False


def game_over(name):
    print(f"Let's try again, {name}!")


def play_game(game_logic_function):
    correct_answers = 0
    attempts = 3

    while correct_answers < attempts:
        if game_logic_function():
            correct_answers += 1
        else:
            return False

    return True
