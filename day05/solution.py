from collections import defaultdict
import copy
from tqdm import tqdm

FILENAME = "test"

with open(f"{FILENAME}.txt") as input_file:
    lines = [l.strip() for l in input_file if l.strip()]

seeds = [int(s) for s in lines.pop(0).replace("seeds: ", "").split(" ")]

state_map = defaultdict(list)

last_state_name = None

while lines:
    line = lines.pop(0)

    if not line[0].isdigit():
        if last_state_name:
            state_map[last_state_name].sort(key=lambda x: x[0])
        last_state_name = line.replace(" map:", "")
    else:
        state_map[last_state_name].append([int(n) for n in line.split(" ")])


def convert_seeds(seeds):
    for _, conversions in state_map.items():
        for seed_i in range(len(seeds)):
            seed = seeds[seed_i]
            for conversion in conversions:
                dest_start, source_start, scope = conversion

                if source_start <= seed < source_start + scope:
                    new_seed_value = seed - source_start + dest_start
                    seeds[seed_i] = new_seed_value
                    break
    return seeds


print("Part 1", sorted(convert_seeds(copy.copy(seeds)))[0])


def expand_seeds(seeds):
    all_seeds = set()
    lowest = None

    while seeds:
        print("OG SEEDS LEFT", len(seeds))
        start, scope = seeds.pop(0), seeds.pop(0)
        new_seeds = set(range(start, start + scope)).difference(all_seeds)
        all_seeds = all_seeds.union(new_seeds)
        print("Gonna expand", len(new_seeds), "seeds")
        for seed in tqdm(new_seeds):
            for _, conversions in state_map.items():
                for conversion in conversions:
                    dest_start, source_start, scope = conversion

                    if source_start <= seed < source_start + scope:
                        new_seed_value = seed - source_start + dest_start
                        seed = new_seed_value
                        break
            if lowest is None or seed < lowest:
                lowest = seed
    print(lowest)


print("Expanding them seeds...")
expanded_seeds = expand_seeds(seeds)

print("Converted the seeds! Getting smaller one...")
