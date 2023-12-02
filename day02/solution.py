import copy
from collections import defaultdict
from functools import reduce

mul = lambda x: reduce(lambda a, b: a * b, x)

FILENAME = "input"

with open(f"{FILENAME}.txt") as input_file:
    lines = [l.strip() for l in input_file if l.strip()]

games = []

for line in lines:
    game_id, rest = line.split(":")
    game_id = int(game_id.replace("Game ", ""))

    dice_sets = [
        [dice.strip().split(" ") for dice in dice_set.split(",")]
        for dice_set in rest.strip().replace(", ", ",").split(";")
    ]
    games.append((game_id, dice_sets))

part_1_contrains = {"red": 12, "green": 13, "blue": 14}

part_1_score = 0
part_2_score = 0

for game_id, dice_sets in games:
    possible = True
    max_dices = defaultdict(int)

    for dice_set in dice_sets:
        contraints = copy.copy(part_1_contrains)
        for dice in dice_set:
            num, color = dice
            num = int(num)
            contraints[color] -= num

            max_dices[color] = max(max_dices[color], num)

            if contraints[color] < 0:
                possible = False

    if possible:
        part_1_score += game_id

    part_2_score += mul(max_dices.values())

print("Part 1:", part_1_score)
print("Part 2:", part_2_score)
