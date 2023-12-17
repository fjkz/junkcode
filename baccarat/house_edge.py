from collections import namedtuple
from copy import copy
from itertools import product
from functools import reduce

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

def p_cards_from_deck(cards, deck):
    """Probability where `cards` are hit from `deck`."""
    deck = copy(deck)
    p = 1.0
    for c in cards:
        if deck[c] <= 0:
            return 0.0
        p *= deck[c] / sum(deck)
        deck[c] -= 1
    return p

def probability_of_hand(deck):
    # probabilities where player and banker have the hands
    # under the given deck
    p_hand = dict()

    # For all first two pairs
    for p1, p2, b1, b2 in product(list(range(10)), repeat=4):

        # total of the first two cards
        p = (p1 + p2) % 10
        b = (b1 + b2) % 10

        # finish at the first two draw
        if p >= 8 or b >= 8 or (6 <= p <= 7 and 6 <= b <= 7):
            hand = Hand(player=(p1,p2,None), banker=(b1,b2,None))
            p_hand[hand] = p_cards_from_deck([p1,p2,b1,b2], deck)
            continue

        # player hits third card
        if p <= 5:
            for p3 in range(10):
                # judge if banker shall hit the next card along the table
                if HIT_TABLE[b][p3]:
                    for b3 in range(10):
                        hand = Hand(player=(p1,p2,p3), banker=(b1,b2,b3))
                        p_hand[hand] = p_cards_from_deck([p1,p2,p3,b1,b2,b3], deck)
                    continue

                # banker doesn't hit third card
                hand = Hand(player=(p1,p2,p3), banker=(b1,b2,None))
                p_hand[hand] = p_cards_from_deck([p1,p2,p3,b1,b2], deck)
            continue

        # only banker hits third card
        for b3 in range(10):
            hand = Hand(player=(p1,p2,None), banker=(b1,b2,b3))
            p_hand[hand] = p_cards_from_deck([p1,p2,b1,b2,b3], deck)

    return p_hand

# Assume 8 decks
NDECK = 8
deck8 = [4 * 4 * NDECK] + [4 * NDECK for i in range(1, 10)]
p_hand = probability_of_hand(deck8)
assert abs(sum(p_hand.values()) - 1) < 0.1**10

print("Number of hand state", len(p_hand))

def point(hand):
    return sum(card for card in hand if card) % 10

def player_rate(p_hand):
    return sum(p for h, p in p_hand.items() if point(h.player) > point(h.banker))

def banker_rate(p_hand):
    return sum(p for h, p in p_hand.items() if point(h.player) < point(h.banker))

def tie_rate(p_hand):
    return sum(p for h, p in p_hand.items() if point(h.player) == point(h.banker))

def super6_rate(p_hand):
    return sum(p for h, p in p_hand.items() if point(h.player) < point(h.banker) and point(h.banker) == 6)

print("\nWinning Rate")
print("Player\t%.9f" % player_rate(p_hand))
print("Banker\t%.9f" % banker_rate(p_hand))
print("Tie\t%.9f" % tie_rate(p_hand))
print("Super6\t%.9f" % super6_rate(p_hand))

def player_edge(p_hand):
    return 1 - 2 * player_rate(p_hand) - 1 * tie_rate(p_hand)

def banker_edge(p_hand):
    return 1 - 1.95 * banker_rate(p_hand) - 1 * tie_rate(p_hand)

def banker_nocomission_edge(p_hand):
    super6 = super6_rate(p_hand)
    non6 = banker_rate(p_hand) - super6
    return 1 - 1.5 * super6 - 2 * non6 - 1 * tie_rate(p_hand)

print("\nHouse Edge")
print("Player\t%.9f" % player_edge(p_hand))
print("Banker\t%.9f" % banker_edge(p_hand))
print("Banker (no commission)\t%.9f" % banker_nocomission_edge(p_hand))
print("Tie\t%.9f" % (1 - 8 * tie_rate(p_hand)))
print("Super6\t%.9f" % (1 - 15 * super6_rate(p_hand)))

BANKER_CARDS = {5,6,7,8,9}

def house_edge_under_banker_cards_bias():
    print("\nHouse edge under [5..9] cards bias condition")
    print("\nrate\tplayer\tbanker\tbanker_nc")
    decks_card_bias = []
    for i in range(0, 4 * NDECK): # 4 is number of suits of card ♥♠♣♦
        deck = [None] * 10
        for c in range(10):
            if c in BANKER_CARDS:
                deck[c] = i
            elif c == 0:
                deck[c] = 4 * 4 * NDECK
            else:
                deck[c] = 4 * NDECK
        decks_card_bias.append(deck)
    decks_card_bias.append(deck8)
    for i in range(1, 4 * NDECK + 1):
        deck = [None] * 10
        for c in range(10):
            if c in BANKER_CARDS:
                deck[c] = 4 * NDECK
            elif c == 0:
                deck[c] = 4 * (4 * NDECK - i)
            else:
                deck[c] = 4 * NDECK - i
        decks_card_bias.append(deck)

    for deck in decks_card_bias:
        #print(deck)
        rate = sum(n for card, n in enumerate(deck) if card in BANKER_CARDS) / sum(deck)
        pp = probability_of_hand(deck)
        g = "%.4f"
        print(
            "%.3f" % rate,
            g % player_edge(pp), g % banker_edge(pp), g % banker_nocomission_edge(pp),
            sep="\t"
        )

def house_edge_under_icards_are_hit_from_deck():
    print("\nHouse edge when i-cards are hit from deck")
    for card in range(0, 10):
        print(f"\n{card} card")
        print("hit\tplayer\tbanker\tbanker_nc")
        for i in range(deck8[card] + 1):
            deck = copy(deck8)
            deck[card] -= i
            pp = probability_of_hand(deck)
            g = "%.5f"
            print(
                i,
                g % player_edge(pp), g % banker_edge(pp), g % banker_nocomission_edge(pp),
                sep="\t"
            )

def house_edge_change_when_a_card_is_hit():
    p_hand0 = probability_of_hand(deck8)
    player0 = player_edge(p_hand0)
    banker0 = banker_edge(p_hand0)
    banker_nc0 = banker_nocomission_edge(p_hand0)

    print("\nHouse edge change when a i-card is hit from deck")
    print("card\tplayer\tbanker\tbanker_nc")
    for card in range(0, 10):
        deck1 = copy(deck8)
        deck1[card] -= 1
        p_hand1 = probability_of_hand(deck1)
        player1 = player_edge(p_hand1)
        banker1 = banker_edge(p_hand1)
        banker_nc1 = banker_nocomission_edge(p_hand1)
        g = "%.8f"
        print(
            card,
            g % (player1 - player0), g % (banker1 - banker0), g % (banker_nc1 - banker_nc0),
            sep="\t"
        )

#house_edge_under_banker_cards_bias()
#house_edge_under_icards_are_hit_from_deck()
house_edge_change_when_a_card_is_hit()
