from collections import namedtuple
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

def probability_of_hand(p_cards):
    # probability where player and banker have the hands
    # under the distribution of p_cards
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

    return p_hand

def point(hand):
    return sum(card for card in hand if card) % 10

def initial(hand):
    return sum(hand[:2]) % 10

def hit3rd(hand):
    return hand[2] is not None

p_hand = probability_of_hand(p_cards)
assert abs(sum(p_hand.values()) - 1) < 0.1**10

print("Number of hand state", len(p_hand))

print("\nWinner")
player_rate = sum(p for h, p in p_hand.items() if point(h.player) > point(h.banker))
print("Player %.9f" % player_rate)
banker_rate = sum(p for h, p in p_hand.items() if point(h.player) < point(h.banker))
print("Banker %.9f" % banker_rate)
tie_rate = sum(p for h, p in p_hand.items() if point(h.player) == point(h.banker))
print("Tie %.9f" % tie_rate)

print()
super6_rate = sum(p for h, p in p_hand.items() if point(h.player) < point(h.banker) and point(h.banker) == 6)
print("Super6 %.9f" % super6_rate)
non6_rate = sum(p for h, p in p_hand.items() if point(h.player) < point(h.banker) and point(h.banker) != 6)
print("Non6 %.9f" % non6_rate)

print("\nHouse Edge")
notie_rate = 1 - tie_rate
print("Player %.9f" % (1 - 2 * player_rate / notie_rate))
print("Banker %.9f" % (1 - 1.95 * banker_rate / notie_rate))
print("Banker (no commission) %.9f" % (1 - (1.5 * super6_rate + 2 * non6_rate) / notie_rate))
print("Tie %.9f" % (1 - 8 * tie_rate))

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

print("\nCard Rate - 1")
def count_card(hands):
    card_rate = [0.0] * 10
    for cards, percentage in hands:
        for card in cards:
            card_rate[card] += percentage / len(cards)
    # normalize
    total = sum(card_rate)
    for i, r in enumerate(card_rate):
        if i == 0:
            card_rate[i] = r/total*13/4 - 1
            continue
        card_rate[i] = r/total*13 - 1
    return card_rate

hands_all = [
    ([card for card in h.player + h.banker if card is not None], p)
    for h, p in p_hand.items()
]
hands_player_win = [
    ([card for card in h.player + h.banker if card is not None], p)
    for h, p in p_hand.items()
    if point(h.player) > point(h.banker)
]
card_count_player_win = count_card(hands_player_win)

hands_banker_win = [
    ([card for card in h.player + h.banker if card is not None], p)
    for h, p in p_hand.items()
    if point(h.player) < point(h.banker)
]
card_count_banker_win = count_card(hands_banker_win)

hands_super6 = [
    ([card for card in h.player + h.banker if card is not None], p)
    for h, p in p_hand.items()
    if point(h.player) < point(h.banker) and point(h.banker) == 6
]
card_count_super6 = count_card(hands_super6)

hands_non6 = [
    ([card for card in h.player + h.banker if card is not None], p)
    for h, p in p_hand.items()
    if point(h.player) < point(h.banker) and point(h.banker) != 6
]
card_count_non6 = count_card(hands_non6)

hands_tie = [
    ([card for card in h.player + h.banker if card is not None], p)
    for h, p in p_hand.items()
    if point(h.player) == point(h.banker)
]
card_count_tie = count_card(hands_tie)

print("","player","banker", "super6", "non6", "tie", "pl-bn", "n6-pl", sep="\t")
for i, (p, b, s6, n6, t) in enumerate(zip(
    card_count_player_win,
    card_count_banker_win,
    card_count_super6,
    card_count_non6,
    card_count_tie
)):
    f = "% .3f"
    print(i,
        f % p, f % b, f % s6, f % n6, f % t, f % (p-b), f % (n6-p),
        sep="\t")

print("\nWinning Rate under Deck without i-Card")
print("", "player", "banker", "super6", "non6", "tie", "edg_p", "edg_b", "edg_bnc", sep="\t")
for i in range(10):
    # woi: without i-card
    all_woi = sum(p for hand, p in hands_all if i not in hand)
    player_rate_woi = sum(p for hand, p in hands_player_win if i not in hand)/all_woi
    banker_rate_woi = sum(p for hand, p in hands_banker_win if i not in hand)/all_woi
    super6_rate_woi = sum(p for hand, p in hands_super6 if i not in hand)/all_woi
    non6_rate_woi = sum(p for hand, p in hands_non6 if i not in hand)/all_woi
    tie_rate_woi = sum(p for hand, p in hands_tie if i not in hand)/all_woi

    p = player_rate_woi/player_rate - 1
    b = banker_rate_woi/banker_rate - 1
    s6 = super6_rate_woi/super6_rate - 1
    n6 = non6_rate_woi/non6_rate - 1
    t = tie_rate_woi/tie_rate - 1

    notie_rate_woi = 1 - tie_rate_woi
    edge_player = 1 - (2 * player_rate_woi) / notie_rate_woi
    edge_banker = 1 - (1.95 * banker_rate_woi) / notie_rate_woi
    edge_banker_nc = 1 - (1.5 * super6_rate_woi + 2 * non6_rate_woi) / notie_rate_woi

    f = "% .3f"
    g = "% .3f"
    print(
        i,
        f % p, f % b, f % s6, f % n6, f % t,
        g % edge_player, g % edge_banker, g % edge_banker_nc,
        sep="\t"
    )

last5 = [5,6,7,8,9]
all_woi = sum(p for hand, p in hands_all if all(i not in hand for i in last5))
player_rate_woi = sum(p for hand, p in hands_player_win if all(i not in hand for i in last5))/all_woi
banker_rate_woi = sum(p for hand, p in hands_banker_win if all(i not in hand for i in last5))/all_woi
super6_rate_woi = sum(p for hand, p in hands_super6 if all(i not in hand for i in last5))/all_woi
non6_rate_woi = sum(p for hand, p in hands_non6 if all(i not in hand for i in last5))/all_woi
tie_rate_woi = sum(p for hand, p in hands_tie if all(i not in hand for i in last5))/all_woi

p = player_rate_woi/player_rate - 1
b = banker_rate_woi/banker_rate - 1
s6 = super6_rate_woi/super6_rate - 1
n6 = non6_rate_woi/non6_rate - 1
t = tie_rate_woi/tie_rate - 1

notie_rate_woi = 1 - tie_rate_woi
edge_player = 1 - (2 * player_rate_woi) / notie_rate_woi
edge_banker = 1 - (1.95 * banker_rate_woi) / notie_rate_woi
edge_banker_nc = 1 - (1.5 * super6_rate_woi + 2 * non6_rate_woi) / notie_rate_woi

f = "% .3f"
g = "% .3f"
print(
    "5-9",
    f % p, f % b, f % s6, f % n6, f % t,
    g % edge_player, g % edge_banker, g % edge_banker_nc,
    sep="\t"
)


print("\nSensitivity to i-Card")
for bias_card in range(0, 10):
    print(f"\nWinning rate under {bias_card}-card bias condition")
    print("bias", "player", "banker", "super6", "tie", "edg_p", "edg_b", "edg_bnc", sep="\t")
    cases = [round(i * 0.1, 1) for i in range(-10, 11, 5)]
    for bias_rate in cases:

        def p_cards_bias(*cards):
            """Probability where given cards are hit."""
            num_card = [4] + [1 for i in range(1, 10)]
            num_card[bias_card] *= (1 + bias_rate)
            total = sum(num_card)
            p = [n / total for n in num_card]
            return reduce(lambda x, y: x*y, [p[c] for c in cards])

        p_hand_bias = probability_of_hand(p_cards_bias)

        # each rate
        p = sum(p for h, p in p_hand_bias.items() if point(h.player) > point(h.banker))
        b = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker))
        t = sum(p for h, p in p_hand_bias.items() if point(h.player) == point(h.banker))
        s6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) == 6)
        n6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) != 6)
        nt = 1 - t

        # edge
        ep = 1 - 2 * p / nt
        eb = 1 - 1.95 * b / nt
        ebnc = 1 - (1.5 * s6 + 2 * n6) / nt

        f = "%.4f"
        g = "%.4f"
        print(
            "% .1f" % bias_rate,
            f % p, f % b, f % s6, f % t,
            g % ep, g % eb, g % ebnc,
            sep="\t"
        )

print("\nSensitivity to i-Card")
for bias_rate in [-0.5, 0.5]:
    print(f"\nHouse edge under card {bias_rate} bias condition")
    print("card", "edg_p", "edg_b", "edg_bnc", sep="\t")
    for bias_card in range(0, 10):

        def p_cards_bias(*cards):
            """Probability where given cards are hit."""
            num_card = [4] + [1 for i in range(1, 10)]
            num_card[bias_card] *= (1 + bias_rate)
            total = sum(num_card)
            p = [n / total for n in num_card]
            return reduce(lambda x, y: x*y, [p[c] for c in cards])

        p_hand_bias = probability_of_hand(p_cards_bias)

        # each rate
        p = sum(p for h, p in p_hand_bias.items() if point(h.player) > point(h.banker))
        b = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker))
        t = sum(p for h, p in p_hand_bias.items() if point(h.player) == point(h.banker))
        s6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) == 6)
        n6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) != 6)
        nt = 1 - t

        # edge
        ep = 1 - 2 * p / nt
        eb = 1 - 1.95 * b / nt
        ebnc = 1 - (1.5 * s6 + 2 * n6) / nt

        g = "%.4f"
        print(
            bias_card,
            g % ep, g % eb, g % ebnc,
            sep="\t"
        )

print("\nSensitivity to i-Card")
print(f"\nHouse edge change with card")
print("card", "edg_p", "edg_b", "edg_bnc", sep="\t")
for bias_card in range(0, 10):
    ep = [0] * 2
    eb = [0] * 2
    ebnc = [0] * 2

    for i, bias_rate in enumerate([-0.5, 0.5]):

        def p_cards_bias(*cards):
            """Probability where given cards are hit."""
            num_card = [4] + [1 for i in range(1, 10)]
            num_card[bias_card] *= (1 + bias_rate)
            total = sum(num_card)
            p = [n / total for n in num_card]
            return reduce(lambda x, y: x*y, [p[c] for c in cards])

        p_hand_bias = probability_of_hand(p_cards_bias)

        # each rate
        p = sum(p for h, p in p_hand_bias.items() if point(h.player) > point(h.banker))
        b = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker))
        t = sum(p for h, p in p_hand_bias.items() if point(h.player) == point(h.banker))
        s6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) == 6)
        n6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) != 6)
        nt = 1 - t

        # edge
        ep[i] = 1 - 2 * p / nt
        eb[i]  = 1 - 1.95 * b / nt
        ebnc[i] = 1 - (1.5 * s6 + 2 * n6) / nt

    g = "%.4f"
    print(
        bias_card,
        g % (ep[1] - ep[0]), g % (eb[1] - eb[0]), g % (ebnc[1] - ebnc[0]),
        sep="\t"
    )

print("\nSensitivity of 5-9 cards to house edge")
print("card_rate", "edg_p", "edg_b", "edg_bnc", sep="\t")
for n_positive_cards in [i for i in range(0, 14, 1)]:
    # n_positive_cards = 0: no 5-9 card
    # n_positive_cards = 13: all 5-9 card
    rate = n_positive_cards / 13

    def p_cards_bias(*cards):
        """Probability where given cards are hit."""
        num_card = [(13 - n_positive_cards) / 8 for i in range(0, 5)] + [n_positive_cards / 5 for i in range(5, 10)]
        num_card[0] *= 4
        total = sum(num_card)
        p = [n / total for n in num_card]
        return reduce(lambda x, y: x*y, [p[c] for c in cards])

    p_hand_bias = probability_of_hand(p_cards_bias)

    # each rate
    p = sum(p for h, p in p_hand_bias.items() if point(h.player) > point(h.banker))
    b = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker))
    t = sum(p for h, p in p_hand_bias.items() if point(h.player) == point(h.banker))
    s6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) == 6)
    n6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) != 6)
    nt = 1 - t

    # edge
    ep = 1 - 2 * p / nt
    eb = 1 - 1.95 * b / nt
    ebnc = 1 - (1.5 * s6 + 2 * n6) / nt

    g = "%.4f"
    print(
        "%.3f" % rate,
        g % ep, g % eb, g % ebnc,
        sep="\t"
    )

print("\nSensitivity of 5,7,8,9 cards to house edge")
print("card_rate", "edg_p", "edg_b", "edg_bnc", sep="\t")
positive_cards = [5,7,8,9]
negative_cards = [0,1,2,3,4,6]
for n_positive_cards in [i for i in range(0, 14, 1)]:
    # n_positive_cards = 0: no 5-9 card
    # n_positive_cards = 13: all 5-9 card
    rate = n_positive_cards / 13

    def p_cards_bias(*cards):
        """Probability where given cards are hit."""
        num_card = [4] + [1 for i in range(1, 10)]
        for i in range(0, 10):
            if i in positive_cards:
                num_card[i] *= n_positive_cards / len(positive_cards)
            else:
                num_card[i] *= (13 - n_positive_cards) / (13 - len(positive_cards))

        total = sum(num_card)
        p = [n / total for n in num_card]
        return reduce(lambda x, y: x*y, [p[c] for c in cards])

    p_hand_bias = probability_of_hand(p_cards_bias)

    # each rate
    p = sum(p for h, p in p_hand_bias.items() if point(h.player) > point(h.banker))
    b = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker))
    t = sum(p for h, p in p_hand_bias.items() if point(h.player) == point(h.banker))
    s6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) == 6)
    n6 = sum(p for h, p in p_hand_bias.items() if point(h.player) < point(h.banker) and point(h.banker) != 6)
    nt = 1 - t

    # edge
    ep = 1 - 2 * p / nt
    eb = 1 - 1.95 * b / nt
    ebnc = 1 - (1.5 * s6 + 2 * n6) / nt

    g = "%.4f"
    print(
        "%.3f" % rate,
        g % ep, g % eb, g % ebnc,
        sep="\t"
    )
