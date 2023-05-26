import random


def task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def game_even_logic():
    number = random.randint(1, 100)
    question = f"Question: {number}"
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
