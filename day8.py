from dataclasses import dataclass
from copy import deepcopy
from typing import Tuple


@dataclass
class Direction:
    left: str
    right: str


def parse_input() -> Tuple[str, dict[str, Direction]]:

    directions: dict[str, Direction] = {}

    steps = ""
    with open("day8input.txt", "r") as f:
        lines = f.readlines()
        steps = lines[0].strip()

        for i in range(2, len(lines)):
            pos = lines[i][0:3]
            left = lines[i][7:10]
            right = lines[i][12:15]

            directions[pos] = Direction(left, right)

    return steps, directions


if __name__ == "__main__":
    steps, directions = parse_input()

    # print(steps)
    # for k,v in directions.items():
    #     print(f"{k} - ({v.left}, {v.right})")

    num_steps = 0
    step_index = 0
    pos = "AAA"
    while True:
        if steps[step_index] == 'L':
            pos = directions[pos].left
        elif steps[step_index] == 'R':
            pos = directions[pos].right
        else:
            raise Exception("lmao")

        num_steps += 1

        if pos == "ZZZ":
            break

        step_index += 1
        step_index %= len(steps)

    print(num_steps)
