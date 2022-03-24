"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [n**2 for n in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number) -> bool:
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False

    for a in range(3, int(number / 2) + 1, 2):
        if number % a == 0:
            return False
    else:
        return True


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    result = []
    if filter_type == EVEN:
        result = list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == ODD:
        result = list(filter(lambda x: x % 2 != 0, numbers))
    elif filter_type == PRIME:
        result = list(filter(is_prime, numbers))

    return result
