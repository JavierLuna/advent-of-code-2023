from collections import Counter
from functools import cache, cmp_to_key
import itertools

FILENAME = "input"

with open(f"{FILENAME}.txt") as input_file:
    lines = [l.strip() for l in input_file if l.strip()]

CARD_VALUES_P1 = "AKQJT98765432"
CARD_VALUES_P2 = "AKQT98765432J"


def get_hand_type_p1(cards):
    counter = sorted(Counter(cards).items(), key=lambda x: x[1], reverse=True)

    if len(counter) == 1:
        return 0  # Five of a kind

    if counter[0][1] == 4:
        return 1  # Four of a kind

    if counter[0][1] == 3:
        if counter[1][1] == 2:
            return 2  # Full house
        else:
            return 3  # Three of a kind
    if counter[0][1] == 2:
        if counter[1][1] == 2:
            return 4  # Two pairs
        else:
            return 5  # One pair
    return 6  # High card


HAND_TYPES = [
    "Five of a kind",
    "Four of a kind",
    "Full House",
    "Three of a kind",
    "Two pairs",
    "One pair",
    "High card",
]


@cache
def get_hand_type_J(og_cards):
    score = get_hand_type_p1(og_cards)

    if score == 0 or "J" not in og_cards:
        return score

    cards = og_cards.replace("J", "")

    for combination in itertools.combinations(CARD_VALUES_P1 * 4, 5 - len(cards)):
        new_cards = cards + "".join(combination)
        new_score = get_hand_type_p1(new_cards)
        if new_score < score:
            score = new_score
    return score


def get_sorter(get_hand_type_fn, card_values):
    def sort_hands(hand1, hand2):
        cards_1, _ = hand1
        cards_2, _ = hand2

        hand_type_1 = get_hand_type_fn(cards_1)
        hand_type_2 = get_hand_type_fn(cards_2)

        if hand_type_1 == hand_type_2:
            i = 0
            while i < len(cards_1):
                c_1, c_2 = cards_1[i], cards_2[i]
                if c_1 == c_2:
                    i += 1
                    continue
                return -1 if card_values.index(c_1) < card_values.index(c_2) else 1
        return -1 if hand_type_1 < hand_type_2 else 1

    return sort_hands


hands = []


for l in lines:
    cards, bidding = l.split(" ")
    bidding = int(bidding)
    hands.append((cards, bidding))

part_1_score = 0
part_2_score = 0

for rank, hand in enumerate(
    sorted(
        hands,
        key=cmp_to_key(get_sorter(get_hand_type_p1, CARD_VALUES_P1)),
        reverse=True,
    )
):
    part_1_score += (rank + 1) * hand[1]
print("Part 1", part_1_score)

for rank, hand in enumerate(
    sorted(
        hands, key=cmp_to_key(get_sorter(get_hand_type_J, CARD_VALUES_P2)), reverse=True
    )
):
    part_2_score += (rank + 1) * hand[1]
print("Part 2", part_2_score)
