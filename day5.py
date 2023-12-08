from dataclasses import dataclass
from copy import deepcopy
from typing import Tuple


@dataclass
class MapRange:
    src: int
    dst: int
    range: int


@dataclass
class Mapping:
    ranges: list[MapRange]


def parse_input() -> Tuple[list[int], list[Mapping]]:
    seeds: list[int] = []
    mappings: list[Mapping] = []
    with open("day5input.txt", "r") as f:
        lines = f.readlines()

        # seeds
        raw_seeds = lines[0][7:].split(" ")

        for rs in raw_seeds:
            seed = (int(rs.strip()))
            seeds.append(seed)

        current_mapping: Mapping = Mapping([])
        i = 3
        while (i < len(lines)):
            line = lines[i]
            if len(line) < 2:
                mappings.append(deepcopy(current_mapping))
                current_mapping = Mapping([])
                i += 2
            else:
                parts = lines[i].split(" ")
                range = MapRange(
                    int(parts[1].strip()),
                    int(parts[0].strip()),
                    int(parts[2].strip())
                )
                current_mapping.ranges.append(range)
                i += 1

    return seeds, mappings


def map_seed(seed: int, map_range: MapRange) -> int:
    if seed >= map_range.src:
        if seed <= map_range.src + map_range.range:
            offset = seed - map_range.src
            dest = map_range.dst + offset
            return dest

    return -1


if __name__ == "__main__":
    seeds, maps = parse_input()
    print(len(maps))

    # print(seeds)
    # for m in maps:
    #     print(m.ranges)

    # print(seeds)
    for i in range(0, len(maps)):
        for si in range(0, len(seeds)):
            targed_seed = -1
            for mapping in maps[i].ranges:
                mapped_seed = map_seed(seeds[si], mapping)
                if mapped_seed >= 0:
                    seeds[si] = mapped_seed
                    break

        # print(seeds)

    seeds.sort()
    print(seeds[0])
