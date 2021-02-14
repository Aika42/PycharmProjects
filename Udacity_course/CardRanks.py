

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = []
    for r, s in cards:
        ranks.append('--23456789TJQKA'.index(r))

    # ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

#
# def card_ranks(cards):
#     "Return a list of the ranks, sorted with higher first."
#     ranks = [r for r,s in cards]
#
#     acc = []
#     for r, s in cards:
#         if r == 'A':
#             if sorted(ranks) == ['2', '3', '4', '5', 'A']:
#                 acc.append(1)
#             else:
#                 acc.append(14)
#         elif r == 'K':
#             acc.append(13)
#         elif r == 'Q':
#             acc.append(12)
#         elif r == 'J':
#             acc.append(11)
#         elif r == 'T':
#             acc.append(10)
#         else:
#             acc.append(int(r))
#
#     acc.sort(reverse=True)
#     return acc


def test():
    assert card_ranks(['AC', '3D', '4S', 'KH', '2D']) == [14, 13, 4, 3, 2]
    assert card_ranks(['AC', '2S', '3D', '4C', '5H']) == [5, 4, 3, 2, 1]