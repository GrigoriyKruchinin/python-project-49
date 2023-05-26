import random


def task():
    print('What is the result of the expression?')


def game_calc_logic():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    question = f"Question: {number1} {operator} {number2}"
    correct_answer = str(eval(f"{number1} {operator} {number2}"))
    return question, correct_answer
