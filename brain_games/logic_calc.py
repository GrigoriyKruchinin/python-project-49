import random


def calculate(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def play_calc_game(name):
    correct_answers = 0
    max_rounds = 3

    while correct_answers < max_rounds:
        num1 = random.randint(1, 15)
        num2 = random.randint(1, 15)
        operator_choice = random.choice(['+', '-', '*'])

        question = f"Question: {num1} {operator_choice} {num2}"
        user_answer = input(question + '\nYour answer: ')

        expected_answer = calculate(operator_choice, num1, num2)

        if int(user_answer) == expected_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{expected_answer}'.")
            print("Let's try again!")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    play_calc_game()
