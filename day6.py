from dataclasses import dataclass
from copy import deepcopy
from typing import Tuple


def calc(time: int, distance: int) -> int:

    possibles = 0
    for t in range(1, time):
        traved_time = time - t
        speed = t
        traveled = traved_time * speed
        if traveled > distance:
            possibles += 1

    return possibles


if __name__ == "__main__":
    times = [35937366]
    distances = [212206012011044]

    r = 1
    for i in range(0, len(times)):
        calced = calc(times[i], distances[i])
        r *= calced
        print(calced)

    print(r)

    pass
