"""More comprehension exercises"""


def flip_dict(d):
    """Return a new dictionary that maps the original values to the keys."""
    return {value: key for key, value in d.items()}


def get_ascii_codes(str):
    """Return a dictionary mapping the strings to ASCII codes."""
    return {word: [ord(l) for l in word] for word in str}


def dict_from_truple(tup):
    """Turn three-item tuples into a dictionary of two-valued tuples."""
    return {t[0]: t[1:] for t in tup}


def dict_from_tuple(tup):
    """Turn multi-item tuples into a dictionary of two-valued tuples."""
    return {t[0]: t[1:] for t in tup}

def get_all_factors(numbers):
    """Return a dictionary mapping numbers to their factors."""
    return {number: [n for n in range(1, number + 1) if number % n == 0] for number in numbers}
