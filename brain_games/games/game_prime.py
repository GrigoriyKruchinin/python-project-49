import random
from brain_games.game_logic import check_answer


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(1, 100)
    question = f"Question: {number}"
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def brain_prime_game_logic():
    question, correct_answer = generate_question()

    user_answer = input(f"{question}\nYour answer: ")

    return check_answer(user_answer, correct_answer)
