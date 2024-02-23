import random


def generate_random_numbers():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2


def main():
    while True:
        num1, num2 = generate_random_numbers()
        correct_answer = num1 * num2

        while True:
            user_input = input(f"What  is {num1} times {num2}?(-1 to quite) ")
            if user_input.lower() == '-1':
                print("Thanks for playing! Goodbye.")
                return


if __name__ == "__main__":
    main()
