from collections import Counter
from functools import cmp_to_key

FILENAME = "input"

with open(f"{FILENAME}.txt") as input_file:
    lines = [l.strip() for l in input_file if l.strip()]


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


def sort_hands_p1(hand1, hand2):
    card_values = "AKQJT98765432"
    cards_1, _ = hand1
    cards_2, _ = hand2

    hand_type_1 = get_hand_type_p1(cards_1)
    hand_type_2 = get_hand_type_p1(cards_2)

    if hand_type_1 == hand_type_2:
        i = 0
        while i < len(cards_1):
            c_1, c_2 = cards_1[i], cards_2[i]
            if c_1 == c_2:
                i += 1
                continue
            return -1 if card_values.index(c_1) < card_values.index(c_2) else 1
    return -1 if hand_type_1 < hand_type_2 else 1


hands = []


for l in lines:
    cards, bidding = l.split(" ")
    bidding = int(bidding)
    hands.append((cards, bidding))

part_1_score = 0

for rank, hand in enumerate(sorted(hands, key=cmp_to_key(sort_hands_p1), reverse=True)):
    part_1_score += (rank + 1) * hand[1]
print("Part 1", part_1_score)
