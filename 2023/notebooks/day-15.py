def parse(filename):
    with open(f'../inputs/{filename}.txt') as f:
        initialization_seq = f.read().strip()

    return initialization_seq


def _hash(s):
    curr_val = 0

    for c in s:
        curr_val += ord(c)
        curr_val *= 17
        curr_val %= 256

    return curr_val


def solve1(s):
    return sum([_hash(c) for c in s.split(",")])

print(solve1(parse("test_initialization_seq")) == 1320)
print(solve1(parse("initialization_seq")))

# Part 2
import math
from collections import defaultdict

def solve2(s):
    boxes = defaultdict(list)
    lenses = {}

    for step in s.split(","):
        if "=" in step:
            label, focal_len = step.split("=")
            box = _hash(label)
            if label not in boxes[box]:
                boxes[box].append(label)
                slot = len(boxes[box])
                lenses[label] = [box + 1, slot, int(focal_len)]
            else:
                slot = boxes[box].index(label) + 1
                lenses[label] = [box + 1, slot, int(focal_len)]

        else:
            label = step[:-1]
            box = _hash(label)
            if label in boxes[box]:
                i_label = boxes[box].index(label)
                boxes[box] = boxes[box][:i_label] + boxes[box][i_label+1:]
                del lenses[label]

                # Adjust slot values down for remaining lenses in the box
                for label in boxes[box][i_label+1:]:
                    lenses[label][1] = lenses[label][1] - 1

    answer = 0
    for val in lenses.values():
        answer += math.prod(val)

    return answer

print(solve2(parse("test_initialization_seq")) == 145)
print(solve2(parse("initialization_seq")))
