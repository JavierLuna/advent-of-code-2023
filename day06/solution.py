import re
from math import ceil, sqrt, floor

FILENAME = "input"

with open(f"{FILENAME}.txt") as input_file:
    lines = [l.strip() for l in input_file if l.strip()]

times = [match for match in re.findall(r'\d+', lines.pop(0))]
distances = [match for match in re.findall(r'\d+', lines.pop(0))]

def calculate_ways_to_win(t, d):
    t, d = int(t), int(d)
    upper_bound = (t + sqrt((t**2) - 4*d)) / 2 
    lower_bound = (t - sqrt((t**2) - 4*d)) / 2

    if not upper_bound.is_integer():
        upper_bound = floor(upper_bound)
    else:
        upper_bound = int(upper_bound - 1) 

    if not lower_bound.is_integer():
        lower_bound = ceil(lower_bound)
    else:
        lower_bound = int(lower_bound + 1) 

    return upper_bound - lower_bound + 1


part_1_score = 1
for t, d in zip(times, distances):
    part_1_score *= calculate_ways_to_win(t, d) 

print("Part 1", part_1_score)

print("Part 2", calculate_ways_to_win("".join(times), "".join(distances)))
