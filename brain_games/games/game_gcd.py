import random


def task():
    print('Find the greatest common divisor of given numbers.')


def calculate_gcd(number1, number2):
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


def game_gcd_logic():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"Question: {number1} {number2}"
    correct_answer = str(calculate_gcd(number1, number2))
    return question, correct_answer
