def display_segment(digit):
    list1 = []
    list1 += digit
    Horizontal(list1[0])
    Vertical(list1[5], list1[1])
    Horizontal(list1[6])
    Vertical(list1[4], list1[2])
    Horizontal(list1[3])


def Horizontal(number):
    if number == "1": print(" # # # #")


def Vertical(number, number1):
    if number == "1" and number1 == "1":
        for num in range(4):
            print("#       #")

    elif number == "0" and number1 == "1":
        for num in range(4):
            print("       #")

    elif number == "1" and number1 == "0":
        for num in range(4):
            print("#       ")


def validate_digit(number):
    if number != "0" and number != "1":
        raise ValueError("INVALID NUMBER INPUT")


def on_off_the_segment(numbers):
    if numbers[7] == "0":
        return False
    if numbers[7] == "1":
        return True


numbers = input("Enter the numbers: ")
display_segment(numbers)
