def custom_product(*args):
    """
    Calculates the product of a series of integers without using built-in functions.

    Args:
        *args: Arbitrary number of integer arguments.

    Returns:
        int: The product of all input integers.
    """
    result = 1
    for num in args:
        result *= num
    return result

# Example usage:
print(custom_product(2, 3, 4))  # Output: 24
print(custom_product(5, 6, 7, 8))  # Output: 1680
print(custom_product(10))  # Output: 10 (single argument)
