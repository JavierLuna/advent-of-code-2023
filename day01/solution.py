with open("input.txt") as input_file:
    input_data = [l.strip() for l in input_file] 

part_1_matchers = [(str(n), str(n)) for n in range(1, 10)]

def first_last(line, matchers):
    first = last = None
    og_line = line

    while line:
        matches = [line.find(matcher) for matcher, _ in matchers]
        matches = sorted([(match_position, matcher_index) for matcher_index, match_position in enumerate(matches) if match_position != -1], key=lambda x: x[0])
        if not matches:
            break
        if first == None:
            first = matchers[matches[0][1]][1]
        
        last = matchers[matches[-1][1]][1]
        line = line[1:]

    return int(first+last)


part_2_matchers = part_1_matchers + [(val, str(i+1)) for i, val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])] 

print(f"Part 1: {sum(first_last(line, part_1_matchers) for line in input_data)}")
print(f"Part 2: {sum(first_last(line, part_2_matchers) for line in input_data)}")

