import random
from brain_games.game_logic import check_answer


def is_even(number):
    return number % 2 == 0


def brain_even_game_logic():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"

    question = f"Question: {number}"
    user_answer = input(f"{question}\nYour answer: ")

    return check_answer(user_answer, correct_answer)
