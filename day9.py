from dataclasses import dataclass
from copy import deepcopy
from typing import Tuple


def parse_input() -> list[list[int]]:

    readings: list[list[int]] = []

    with open("day9input.txt", "r") as f:
        lines = f.readlines()
        for l in lines:
            s_numbs = l.strip().split(" ")
            numbs = list(map(lambda s: int(s), s_numbs))
            readings.append(numbs)

    return readings


def predict_sequence(numbs: list[int]) -> int:

    steps: list[list[int]] = []

    steps.append(numbs)

    step_index = 0
    while True:
        new_steps: list[int] = []
        for i in range(0, len(steps[step_index])-1):
            new_steps.append(steps[step_index][i+1] - steps[step_index][i])

        steps.append(new_steps)
        step_index += 1

        step_sum = 0
        for s in steps[step_index]:
            step_sum += s

        if step_sum == 0:
            break

    new_num = 0

    for i in range(len(steps)-2, -1, -1):
        new_num2 = steps[i][0] - new_num
        # print(f"{steps[i][0]} - {new_num} = {new_num2}")
        new_num = new_num2

    print(new_num)
    return new_num


if __name__ == "__main__":
    readings = parse_input()

    result = 0
    for r in readings:
        result += predict_sequence(r)

    print(result)
