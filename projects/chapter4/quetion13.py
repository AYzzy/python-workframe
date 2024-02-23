def product(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(product(2, 3, 4))
print(product(5, 6, 7, 8))
print(product(10,7))