import random


def is_even(number):
    return number % 2 == 0


def play_game(name):
    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ")

        if (user_answer == "yes" and is_even(number)) or (user_answer == "no" and not is_even(number)):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is the wrong answer ;(. Correct answer was '{'yes' if is_even(number) else 'no'}'.")
            print("Let's try again!")
            return

    print(f"Congratulations, {name}!")
