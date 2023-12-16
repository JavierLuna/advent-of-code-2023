import re
from collections import defaultdict
import math

FILENAME = "input"

with open(f"{FILENAME}.txt") as input_file:
    lines = [l.strip() for l in input_file if l.strip()]

instructions = lines.pop(0)

map = defaultdict(dict)

for line in lines:
    node, l, r = re.search(r"(.{3}) = \((.{3}), (.{3})\)", line).groups()

    map[node] = {"L": l, "R": r}


def find_node(starting_node, end_node_condition):
    i = 0
    current_node = starting_node
    while not end_node_condition(current_node):
        current_node = map[current_node][instructions[i % len(instructions)]]
        i += 1

    return i


print(f"Part 1: {find_node('AAA', lambda current_node: current_node == 'ZZZ')}")


def part_2():
    starting_nodes = [node for node in map if node.endswith("A")]
    distances = [
        find_node(node, lambda current_node: current_node.endswith("Z"))
        for node in starting_nodes
    ]
    return math.lcm(*distances)


print(f"Part 2: {part_2()}")
