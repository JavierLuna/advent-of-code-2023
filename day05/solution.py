from collections import defaultdict

FILENAME = "input"

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

for conversion_id, conversions in state_map.items():
    for seed_i in range(len(seeds)):
        seed = seeds[seed_i]
        for conversion in conversions:
            dest_start, source_start, scope = conversion

            if source_start <= seed < source_start + scope:
                new_seed_value = seed - source_start + dest_start
                seeds[seed_i] = new_seed_value
                break
print("Part 1", sorted(seeds)[0])
