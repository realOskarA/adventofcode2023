from dataclasses import dataclass


@dataclass
class Card:
    winning: list[int]
    numbers: list[int]


def parse_input() -> list[Card]:

    cards: list[Card] = []
    with open("day4input.txt", "r") as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            start = l.find(":")+2
            split = l.find("|")
            card = Card([], [])
            for i in range(start, split, 3):
                s_num = l[i] + l[i+1]
                num = int(s_num)
                card.winning.append(num)

            for i in range(split+2, len(l), 3):
                s_num = l[i] + l[i+1]
                num = int(s_num)
                card.numbers.append(num)

            card.winning.sort()
            card.numbers.sort()
            cards.append(card)

    return cards

def eval_card(card: Card) -> int:
    score = 0

    for n in card.numbers:
        if n in card.winning:
            if score == 0:
                score = 1
            else:
                score *= 2

    return score


if __name__ == "__main__":
    cards = parse_input()

    r = 0
    for c in cards:
        r += eval_card(c)

    print(r)

    # for c in cards:
    #     sc = ""
    #     for n in c.winning:
    #         sc += f"{n:>2} "
    #     sc += "| "
    #     for n in c.numbers:
    #         sc += f"{n:>2} "
    #     print(sc)


