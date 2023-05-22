import random


def generate_progression(start, step, length):
    progression = [start]
    for _ in range(length - 1):
        start += step
        progression.append(start)
    return progression


def play_progression_game(name):
    correct_answers = 0

    while correct_answers < 3:
        start = random.randint(1, 19)
        step = random.randint(2, 9)
        length = 10
        progression = generate_progression(start, step, length)
        secret_index = random.randint(0, length - 1)
        expected_answer = progression[secret_index]
        progression[secret_index] = ".."
        question = " ".join(map(str, progression))

        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if int(user_answer) == expected_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{expected_answer}'.")
            print("Let's try again!")
            return

    print(f"Congratulations, {name}!")
