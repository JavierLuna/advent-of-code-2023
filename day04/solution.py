
FILENAME = "input"

with open(f"{FILENAME}.txt") as input_file:
    lines = [l.strip() for l in input_file if l.strip()]

cards = []

for line in lines:
    card_id, numbers = line.split(":")
    card_id = int(card_id.replace("Card ", "")) - 1 
    winning_numbers, my_numbers = numbers.strip().split(" | ")
    winning_numbers = [n.strip() for n in winning_numbers.split(" ") if n.strip()]
    my_numbers = [n.strip() for n in my_numbers.split(" ") if n.strip()]
    cards.append((card_id, winning_numbers, my_numbers))

part_1_score = 0
n_cards = [1] * len(cards) # There's always the OG one

for card in cards:
    card_id, winning_numbers, my_numbers = card
    matching_numbers = len(set(winning_numbers).intersection(my_numbers))
    for to_be_cloned_card_id in range(card_id+1, card_id+1+matching_numbers):
        n_cards[to_be_cloned_card_id] += n_cards[card_id]
    part_1_score += 0 if not matching_numbers else 2 ** (matching_numbers - 1)


print("Part 1",part_1_score)
print("Part 2", sum(n_cards))
