input_sentence = input("Enter a sentence: ")


def count_words():
    letter = 0
    numbers = 0

    for i in input_sentence:
        if i.isalpha():
            letter += 1
        if i.isnumeric():
            numbers += 1

    num_chars = len(input_sentence)

    print(f'There are {letter} letter and {numbers} numbers in the sentence.'
          f' The total number of characters is {num_chars}')


if __name__ == "__main__":
    count_words()


def capitalize_sentence():
    upper = 0
    lower = 0

    for char in input_sentence:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1

    print(f'UPPER CASE {upper} LOWERCASE {lower}')
