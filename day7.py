from dataclasses import dataclass
from copy import deepcopy
from typing import Tuple

VALUE_MAP = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


@dataclass
class Hand:
    hand: str
    cards: list[int]
    rank: int
    bet: int

    def __lt__(self, other):
        if self.rank == other.rank:
            for i in range(0, len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                return other.cards[i] < self.cards[i]

        return self.rank < other.rank


def rank_hand(hand: list[int]) -> int:
    mapped_cards = {}

    for c in hand:
        if c in mapped_cards:
            mapped_cards[c] += 1
        else:
            mapped_cards[c] = 1

    unique = list(mapped_cards.values())
    unique.sort(reverse=True)
    # print(unique)

    num_unique = len(unique)
    if num_unique == 1:
        return 1  # Five of a kind

    if num_unique == 2:
        if unique[0] == 4:
            return 2  # Four of a kind
        if unique[0] == 3 and unique[1] == 2:
            return 3  # Full house

        # return 4 # Three of a kind (not possible?)
        raise Exception("Unexpected")

    if num_unique == 3:
        if unique[0] == 3:
            return 4  # Three of a kind
        if unique[0] == 2 and unique[1] == 2:
            return 5  # Two pair

    if num_unique == 4:
        return 6  # One pair

    return 7  # High card

    # for k,v in mapped_cards.items():
    #     print(k, v)

    return 0


def parse_input() -> list[Hand]:

    hands: list[Hand] = []

    with open("day7input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(" ")

            cards = []
            for c in parts[0].strip():
                cards.append(VALUE_MAP[c])

            # cards.sort(reverse=True)

            rank = rank_hand(cards)
            bet = int(parts[1].strip())

            hands.append(Hand(
                parts[0].strip(),
                cards,
                rank,
                bet
            ))

    return hands


if __name__ == "__main__":
    hands = parse_input()

    hands.sort(reverse=True)
    sum = 0
    for i in range(0, len(hands)):
        mult = i+1
        sum += hands[i].bet * mult

    print(sum)
