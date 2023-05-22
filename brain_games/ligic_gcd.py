import random


def common_divisor(num1, num2):
    min_num = min(num1, num2)
    max_mum = max(num1,num2)
    for i in range(min_num, 1, -1):
        if min_num % i == 0 and max_mum % i == 0:
            return i


def play_gcd_game(name):
    correct_answers = 0

    while correct_answers < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        print(f"Question: {num1} {num2}")
        user_answer = input("Your answer: ")

        expected_answer = common_divisor(num1, num2)

        if int(user_answer) == expected_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{expected_answer}'.")
            print("Let's try again!")
            return
