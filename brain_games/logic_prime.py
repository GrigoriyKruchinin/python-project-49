import random
import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def play_prime_game(name):
    correct_answers = 0

    while correct_answers < 3:
        num = random.randint(1, 100)
        print(f"Question: {num}")
        user_answer = input("Your answer: ")

        if (user_answer == "yes" and is_prime(num)) or \
                (user_answer == "no" and not is_prime(num)):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is the wrong answer ;(. "
                  f"Correct answer was '{'no' if is_prime(num) else 'yes'}'.")
            print("Let's try again!")
            return

    print(f"Congratulations, {name}!")
