# -----------
# User Instructions
#
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    value = True
    for i in range(len(ranks)-1):
        if ranks[i] - 1 != ranks[i+1]:
            value = False
    return value


def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    value = True
    ch = suits[0]
    for suit in suits:
        if ch != suit:
            value = False
    return value


def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'

test()