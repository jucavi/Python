"""Generator Exercises."""


def is_prime(number):
    """Return True if candidate number is prime."""
    return all(number % n != 0 for n in range(2, number))


def all_together(*iters):
    """String together all items from the given iterables."""
    clean_iter = (item for item in iters if item)
    return (item for row in clean_iter for item in row)

def interleave(list1, list2):
    """Return iterable of one item at a time from each list."""
    return (n for tup in zip(list1, list2) for n in tup)

words = {
    'gato': 'cat',
    'el': 'the',
    'esta': 'is',
    'en': 'in',
    'la': 'the',
    'casa': 'house'
}

def translate(sentence):
    """Return a transliterated version of the given sentence."""
    return ' '.join(words[word] for word in sentence.split())


def parse_ranges(str):
    """Return a list of numbers corresponding to number ranges in a string"""
    interval = ([int(n) for n in s.split('-')] for s in str.split(','))
    return (n for r in interval for n in range(r[0], r[1] + 1))

from itertools import count

def first_prime_over(number):
    """Return the first prime number over a given number."""
    return (n for n in count(number + 1) if is_prime(n)).next()
        
            

def is_anagram(phrase1, phrase2):
    """Return True if the given words are anagrams."""
    return all(
        letter in phrase2.lower() and phrase1.lower().count(letter) == phrase2.lower().count(letter)
        for letter in (l for l in phrase1.lower() if l not in "' .,")
    )