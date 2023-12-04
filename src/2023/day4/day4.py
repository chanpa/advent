import re
from collections import Counter

from src.helpers import file_parser


data = file_parser.file_as_line_list(2023, 4)


def part_a():
    points = []
    for card in data:
        winners = get_winners(card)

        if winners:
            points.append(1 * (2 ** (len(winners) - 1)))

    return sum(points)


def part_b():
    cards = Counter(i for i in range(1, len(data) + 1))
    for i, card in enumerate(data):
        winners = get_winners(card)

        for w in range(1, len(winners) + 1):
            cards[i + 1 + w] += 1 * (cards[i + 1])

    return sum(cards.values())


def get_winners(card):
    numbers = card.strip().split(": ")[1]
    winning_numbers, my_numbers = map(
        lambda s: set(map(int, re.findall(r"\d+", s))),
        numbers.split(" | ")
    )
    return my_numbers.intersection(winning_numbers)


if __name__ == "__main__":
    print(part_a())
    print(part_b())
