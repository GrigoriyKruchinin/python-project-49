import random


TASK = 'What is the result of the expression?'


def generate_data():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        question = f"{number1} + {number2}"
        correct_answer = number1 + number2
    elif operator == '-':
        question = f"{number1} - {number2}"
        correct_answer = number1 - number2
    elif operator == '*':
        question = f"{number1} * {number2}"
        correct_answer = number1 * number2

    return question, str(correct_answer)
