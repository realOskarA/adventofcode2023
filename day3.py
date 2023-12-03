from dataclasses import dataclass
from collections import namedtuple

Point = namedtuple('Point', 'x y')


@dataclass
class EngNum:
    id: int
    start: Point
    end: Point


def parse_input() -> list[str]:
    with open("day3input.txt", "r") as f:
        raw_lines = f.readlines()
        return list(map(lambda l: l.strip(), raw_lines))


def parse_engnum(line: str, y) -> list[EngNum]:
    parsed: list[EngNum] = []

    cur_num = ""
    cur_start = -1

    for i in range(0, len(line)):
        if line[i].isnumeric():
            cur_num += line[i]
            if cur_start < 0:
                cur_start = i

        else:
            if cur_start > -1:
                parsed.append(EngNum(
                    int(cur_num),
                    Point(cur_start, y),
                    Point(i-1, y),
                ))
                cur_start = -1
                cur_num = ""

    if cur_start > -1:
        parsed.append(EngNum(
            int(cur_num),
            Point(cur_start, y),
            Point(len(line)-1, y),
        ))

    return parsed


def check_num(numb: EngNum, input: list[str]) -> bool:
    field_max_y = len(input)-1
    field_max_x = len(input[0])-1

    min_y = max(numb.start.y-1, 0)
    min_x = max(numb.start.x-1, 0)

    max_y = min(numb.end.y+1, field_max_y)
    max_x = min(numb.end.x+1, field_max_x)

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            symbol = input[y][x]
            if symbol.isnumeric():
                continue
            if symbol == ".":
                continue

            print("T", numb.id, x, y)
            return True

    print("F", numb.id)
    return False


if __name__ == "__main__":
    input = parse_input()

    numbs: list[EngNum] = []
    for i in range(0, len(input)):
        numbs.extend(parse_engnum(input[i], i))

    r = 0
    for numb in numbs:
        if (check_num(numb, input)):
            r += numb.id

    print(r)
