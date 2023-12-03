from collections import defaultdict
from functools import reduce


FILENAME = "input"

with open(f"{FILENAME}.txt") as input_file:
    lines = [l.strip() for l in input_file if l.strip()]

symbol_coords = defaultdict(lambda: defaultdict(dict))
part_numbers = []

is_symbol = lambda x: x and not x.isdigit() and not x == "."

for line_n, line in enumerate(lines):
    number_buffer = None
    for char_n, char in enumerate(line):
        if is_symbol(char):
            symbol_coords[line_n][char_n] = {"value": char, "references": []}

        if char.isdigit():
            if number_buffer is None:
                number_buffer = {
                    "value": char,
                    "coords": [(line_n, char_n)],
                    "referenced": False,
                }
            else:
                number_buffer["value"] = number_buffer["value"] + char
                number_buffer["coords"].append((line_n, char_n))
        else:
            if number_buffer:
                part_numbers.append(number_buffer)
            number_buffer = None
    if number_buffer:
        part_numbers.append(number_buffer)


def is_part(part_number):
    for line_n, char_n in part_number["coords"]:
        for d_line, d_char in [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, -1),
            (-1, 1),
        ]:
            possible_symbol = symbol_coords[d_line + line_n][d_char + char_n]
            if possible_symbol and is_symbol(possible_symbol["value"]):
                possible_symbol["references"].append(int(part_number["value"]))
                return True


part_1_score = 0

for part_number in part_numbers:
    if is_part(part_number):
        part_1_score += int(part_number["value"])

print("Part 1", part_1_score)
part_2_score = 0

mul = lambda x: reduce(lambda a, b: a * b, x)

for subcoord in symbol_coords.values():
    for symbol in subcoord.values():
        if symbol and symbol["value"] == "*" and len(symbol["references"]) == 2:
            part_2_score += mul(symbol["references"])

print("Part 2", part_2_score)
