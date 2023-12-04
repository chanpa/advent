import re
from collections import Counter

from src.helpers import file_parser


data = file_parser.file_as_line_list(2023, 4)


def part_a():
    points = 0
    for card in data:
        if winners := get_winners(card):
            points += 2 ** (len(winners) - 1)

    return points


def part_b():
    cards = Counter(i + 1 for i in range(len(data)))
    for i, card in enumerate(data):
        for w in range(len(get_winners(card))):
            cards[i + 1 + w + 1] += cards[i + 1]

    return sum(cards.values())


def get_winners(card):
    winning_numbers, my_numbers = map(
        lambda s: set(map(int, re.findall(r"\d+", s))),
        card.strip().split(": ")[1].split(" | ")
    )
    return my_numbers.intersection(winning_numbers)


if __name__ == "__main__":
    print(part_a())
    print(part_b())
