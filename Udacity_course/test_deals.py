# This builds a deck of 52 cards. If you are unfamiliar
# mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

import random


def deck():
    "generates deck of 52 cards and returns not shuffled deck"
    mydeck = []
    cards = ' '.join('23456789TJQKA')
    suits = ' '.join('SHDC')
    cards_list = cards.split()
    suits_list = suits.split()

    for j in range(len(suits_list)):
        for i in range(len(cards_list)):
            mydeck.append(cards_list[i] + suits_list[j])
    return mydeck  # returns not shuffled deck

def random_deck():
    "generates deck of shuffled 52 cards"
    ran_deck = deck()
    random.shuffle(ran_deck)
    return ran_deck  # returns shuffled deck


def deal(numhands: int, numcards: int, f: callable):
    "returns lists for number of hands with number of cards requested"
    deal_deck = f
    acc = []
    m = 0

    for i in range(numhands):
        sl = deal_deck[m: m + numcards]
        acc.append(sl)
        m = m + numcards
    return tuple(acc)


def test_random_deck():
    # tests for random_deck()
    xs = random_deck()
    print(xs)
    assert len(xs) == 52
    assert '3S' in xs and '5H' in xs


def test_deals():
    assert deal(4, 5, f=deck()) == (
    ['2S', '3S', '4S', '5S', '6S'], ['7S', '8S', '9S', 'TS', 'JS'], ['QS', 'KS', 'AS', '2H', '3H'],
    ['4H', '5H', '6H', '7H', '8H'])
    assert len(deal(6, 5, f=random_deck())) == 6
    un = list(deal(4, 5, f=random_deck()))
    for u in un:
        len(set(u)) == 5
    print("Test passed")


