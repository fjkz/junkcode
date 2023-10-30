from collections import namedtuple
from itertools import product

Hand = namedtuple('Hand', ["player", "banker"])

HIT_TABLE = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,0,1],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

def p_cards(*cards):
    """Probability where given cards are hit."""
    # Assume N decks
    N = 8
    deck = [4 * 13 * N] + [13 * N for i in range(1, 10)]

    p = 1.0
    for c in cards:
        if deck[c] <= 0:
            return 0.0
        p *= deck[c] / sum(deck)
        deck[c] -= 1
    return p

# probability where player and banker have the hands
p_hand = dict()

# For all first two pairs
for p1, p2, b1, b2 in product(list(range(10)), repeat=4):

    # total of the first two cards
    p = (p1 + p2) % 10
    b = (b1 + b2) % 10

    # finish at the first two draw
    if p >= 8 or b >= 8 or (6 <= p <= 7 and 6 <= b <= 7):
        hand = Hand(player=(p1,p2,None), banker=(b1,b2,None))
        p_hand[hand] = p_cards(p1,p2,b1,b2)
        continue

    # player hits third card
    if p <= 5:
        for p3 in range(10):
            # judge if banker shall hit the next card along the table
            if HIT_TABLE[b][p3]:
                for b3 in range(10):
                    hand = Hand(player=(p1,p2,p3), banker=(b1,b2,b3))
                    p_hand[hand] = p_cards(p1,p2,p3,b1,b2,b3)
                continue

            # banker doesn't hit third card
            hand = Hand(player=(p1,p2,p3), banker=(b1,b2,None))
            p_hand[hand] = p_hand[hand] = p_cards(p1,p2,p3,b1,b2)
        continue

    # only banker hits third card
    for b3 in range(10):
        hand = Hand(player=(p1,p2,None), banker=(b1,b2,b3))
        p_hand[hand] = p_cards(p1,p2,b1,b2,b3)

def point(hand):
    return sum(card for card in hand if card) % 10

def initial(hand):
    return sum(hand[:2]) % 10

def hit3rd(hand):
    return hand[2] is not None

assert abs(sum(p_hand.values()) - 1) < 0.1**10

print("Number of hand state", len(p_hand))

print("\nWinner")
player_win = sum(p for h, p in p_hand.items() if point(h.player) > point(h.banker))
print("Player %.9f" % player_win)
banker_win = sum(p for h, p in p_hand.items() if point(h.player) < point(h.banker))
print("Banker %.9f" % banker_win)
tie = sum(p for h, p in p_hand.items() if point(h.player) == point(h.banker))
print("Tie %.9f" % tie)

print()
banker_win6 = sum(p for h, p in p_hand.items() if point(h.player) < point(h.banker) and point(h.banker) == 6)
print("Banker w/ 6 %.9f" % banker_win6)
banker_win_no6 = sum(p for h, p in p_hand.items() if point(h.player) < point(h.banker) and point(h.banker) != 6)
print("Banker w/ non-6 %.9f" % banker_win_no6)

print("\nHouse Edge")
no_tie = 1 - tie
print("Player %.9f" % (1 - 2 * player_win / no_tie))
print("Banker %.9f" % (1 - 1.95 * banker_win / no_tie))
print("Banker (no commission) %.9f" % (1 - (1.5 * banker_win6 + 2 * banker_win_no6) / no_tie))
print("Tie %.9f" % (1 - 8 * tie))

print("\nNumber of Cards (Player:Banker)")
print("2:2 %.9f" % sum(p for h, p in p_hand.items() if not hit3rd(h.player) and not hit3rd(h.banker)))
print("3:2 %.9f" % sum(p for h, p in p_hand.items() if hit3rd(h.player) and not hit3rd(h.banker)))
print("2:3 %.9f" % sum(p for h, p in p_hand.items() if not hit3rd(h.player) and hit3rd(h.banker)))
print("3:3 %.9f" % sum(p for h, p in p_hand.items() if hit3rd(h.player) and hit3rd(h.banker)))

print("\nPlayer Win Rate for Banker's First 2 Cards")
for i in range(10):
    pi = {
        h: p for h, p in p_hand.items() if (
            initial(h.banker) == i and
            point(h.player) != point(h.banker)
        )
    }
    # rate where player's total of first 2 cards is i and not tie
    rate_i = sum(pi.values())
    # rate of player win
    rate_p = sum(p for h, p in pi.items() if point(h.player) > point(h.banker))
    print(i, "%.9f" % (rate_p/rate_i))

print("\nBanker Win Rate for Player's First 2 Cards")
for i in range(10):
    pi = {
        h: p for h, p in p_hand.items() if (
            initial(h.player) == i and
            point(h.player) != point(h.banker)
        )
    }
    # rate where player's total of first 2 cards is i and not tie
    rate_i = sum(pi.values())
    # rate of player win
    rate_p = sum(p for h, p in pi.items() if point(h.player) < point(h.banker))
    print(i, "%.9f" % (rate_p/rate_i))

print("\nPlayer Win Rate with Difference of each Total")
for i in range(-7, 8):
    pi = {
        h: p for h, p in p_hand.items() if (
            initial(h.player) - initial(h.banker) == i and
            (hit3rd(h.player) or hit3rd(h.banker)) and
            point(h.player) != point(h.banker)
        )
    }
    rate_i = sum(pi.values())
    rate_p = sum(p for h, p in pi.items() if point(h.player) > point(h.banker))
    print(i, "%.9f" % (rate_p/rate_i))
