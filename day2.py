import re
from dataclasses import dataclass


@dataclass
class Game:
    id: int
    hands: list[dict[str, int]]


def parse_hand(hand: str) -> dict[str, int]:
    r = {}
    parts = hand.split(",")
    for p in parts:
        p = p.strip()
        i = p.find(" ")
        r[p[i+1:]] = int(p[:i])

    return r


def check_round(round: Game) -> bool:
    for h in r.hands:
        if h.get("red", 0) > 12:
            return False

        if h.get("green", 0) > 13:
            return False

        if h.get("blue", 0) > 14:
            return False

    return True


def find_pow(round: Game) -> int:
    mincol = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for h in r.hands:
        mincol["red"] = max(mincol["red"], h.get("red", 0))
        mincol["green"] = max(mincol["green"], h.get("green", 0))
        mincol["blue"] = max(mincol["blue"], h.get("blue", 0))

    return mincol["red"] * mincol["blue"] * mincol["green"]


def parse_input(line: str) -> Game:
    s1 = line.find(":")

    id = int(line[5:s1])

    hands = line[s1+1:].split(";")

    parsed_hands = []
    for h in hands:
        parsed_hands.append(parse_hand(h.strip()))

    return Game(id, parsed_hands)


if __name__ == "__main__":
    rounds: list[Game] = []
    with open("day2input.txt", "r") as f:
        lines = f.readlines()
        for l in lines:
            rounds.append(parse_input(l.strip()))

    result = 0
    for r in rounds:
        result += find_pow(r)

    print(result)
