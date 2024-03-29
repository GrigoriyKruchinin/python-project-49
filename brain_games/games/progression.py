import random


TASK = 'What number is missing in the progression?'


def generate_data():
    start = random.randint(1, 10)
    diff = random.randint(2, 9)
    length = 10
    progression = [str(start + diff * i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = f"{' '.join(progression)}"
    return question, correct_answer
