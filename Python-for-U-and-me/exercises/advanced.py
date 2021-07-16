"""Advanced exercises"""
from collections import namedtuple
import csv

import random


def matrix_from_string(string):
    """Convert rows of numbers to list of lists."""
    return [[int(el) for el in row.split()] for row in string.split('\n')]

def parse_csv(file_obj):
    """Return namedtuple list representing data from given file object."""
    csv_row = csv.reader(file_obj)
    Row = namedtuple('Row', next(csv_row))
    return (Row._make(row) for row in csv_row)
     
   


def get_cards():
    """Create a list of namedtuples representing a deck of playing cards."""
    Card = namedtuple('Card', ['rank', 'suit'])
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    return [Card._make([rank, suit]) for suit in suits for rank in ranks]


def shuffle_cards(deck):
    """Shuffles a list in-place"""
    random.shuffle(deck)


def deal_cards(deck, count=5):
    """Remove the given number of cards from the deck and returns them"""
    return [deck.pop() for _ in range(5)]