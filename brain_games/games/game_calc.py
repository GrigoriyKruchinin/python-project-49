import random


TASK = 'What is the result of the expression?'


def generation():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        question = f"{number1} + {number2}"
        correct_answer = str(number1 + number2)
    elif operator == '-':
        question = f"{number1} - {number2}"
        correct_answer = str(number1 - number2)
    else:
        question = f"{number1} * {number2}"
        correct_answer = str(number1 * number2)

    return question, correct_answer
