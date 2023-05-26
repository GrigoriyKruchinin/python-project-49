import random


def task():
    print('What number is missing in the progression?')


def game_progression_logic():
    start = random.randint(1, 10)
    diff = random.randint(2, 9)
    length = 10
    progression = [str(start + diff * i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = f"Question: {' '.join(progression)}"
    return question, correct_answer
