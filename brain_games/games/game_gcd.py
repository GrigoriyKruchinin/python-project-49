import random
from brain_games.game_logic import check_answer


def calculate_gcd(number1, number2):
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"Question: {number1} {number2}"
    correct_answer = str(calculate_gcd(number1, number2))
    return question, correct_answer


def brain_gcd_game_logic():
    question, correct_answer = generate_question()

    user_answer = input(f"{question}\nYour answer: ")

    return check_answer(user_answer, correct_answer)
