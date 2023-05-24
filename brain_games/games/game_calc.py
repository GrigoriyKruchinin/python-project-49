import random
from brain_games.game_logic import check_answer


def generate_question():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    question = f"Question: {number1} {operator} {number2}"
    correct_answer = str(eval(f"{number1} {operator} {number2}"))
    return question, correct_answer


def brain_calc_game_logic():
    question, correct_answer = generate_question()

    user_answer = input(f"{question}\nYour answer: ")

    return check_answer(user_answer, correct_answer)
