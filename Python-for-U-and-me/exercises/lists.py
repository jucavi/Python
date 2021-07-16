"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    return [name for name in names if name[0].lower() in 'aeiou']


def power_list(numbers):
    """Return a list that contains each number raised to the i-th power."""
    return [number ** power for power, number in enumerate(numbers)]


def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [item for row in matrix for item in row]


def reverse_difference(list):
    """Return list subtracted from the reverse of itself."""
    return [a - b for a, b in zip(list, list[::-1])]


def matrix_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    return [[i1 + i2 for i1, i2 in zip(a1, a2)] for a1, a2 in zip(matrix1, matrix2)]


def transpose(matrix):
    """Return a transposed version of given list of lists."""
    return [list(row) for row in zip(*matrix)]


def get_factors(number):
    """Return a list of all factors of the given number."""
    return [d for d in range(1,number + 1) if number % d == 0]


import math
def triples(number):
    """Return list of Pythagorean triples less than input num."""
    return [
        (a, b, int(math.sqrt(a**2 + b**2)))
        for a in range(1, number)
        for b in range(a, number)
        if math.sqrt(a**2 + b**2) < number and int(math.sqrt(a**2 + b**2)) == math.sqrt(a**2 + b**2)
    ]
