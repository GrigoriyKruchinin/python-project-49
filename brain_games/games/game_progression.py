import random
from brain_games.game_logic import check_answer


def generate_progression():
    start = random.randint(1, 10)
    diff = random.randint(2, 9)
    length = 10
    progression = [str(start + diff * i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = f"Question: {' '.join(progression)}"
    return question, correct_answer


def brain_progression_game_logic():
    question, correct_answer = generate_progression()

    user_answer = input(f"{question}\nYour answer: ")

    return check_answer(user_answer, correct_answer)
