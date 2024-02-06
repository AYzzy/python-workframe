sample_list = list(range(10, 20))


def get_total(numbers):
    total = 0
    for number in numbers:
        total += 1
    return total


def get_sum_of_even_numbers(numbers):
    return sum(numbers[1::2])


def get_sum_of_odd(numbers):
    return sum(numbers[::2])


def get_product_of_third_element(numbers):
    product = 1
    for index in range(2, len(numbers), 3):
        product *= numbers[index]
    return product


def get_average(numbers):
    total =0
    for number in numbers:
        total += numbers
        average = total / get_total(numbers)
    return average


# def sumz(numbers);
#     total = 0
#     for num in numz:
#         total+=numz
#     return total


def get_largest_number(numbers):
    largest = numbers[0]
    for element in numbers:
        if element > largest:
            largest = element
    return largest


def get_smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def get_string(words):
    result =[]
    for word in words:
        if len(word) >= 2:
            if len(word) >= 2 and word[0] == word[-1]:
                result.append(word)
    return result