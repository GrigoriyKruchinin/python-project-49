import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_data():
    number = random.randint(1, 100)
    question = f"{number}"
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
