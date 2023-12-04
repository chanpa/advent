import re
from collections import Counter

from src.helpers import file_parser


data = file_parser.file_as_line_list(2023, 4)


def part_a():
    points = []
    for i, line in enumerate(data):
        card, numbers = line.strip().split(": ")
        winning_numbers_str, my_numbers_str = numbers.split(" | ")
        winning_numbers = set(map(int, re.findall(r"\d+", winning_numbers_str)))
        my_numbers = set(map(int, re.findall(r"\d+", my_numbers_str)))
        winners = my_numbers.intersection(winning_numbers)

        if winners:
            points.append(1 * (2 ** (len(winners) - 1)))

    return sum(points)


def part_b():
    cards = Counter(i for i in range(1, len(data) + 1))
    for i, line in enumerate(data):
        card, numbers = line.strip().split(": ")
        winning_numbers_str, my_numbers_str = numbers.split(" | ")
        winning_numbers = set(map(int, re.findall(r"\d+", winning_numbers_str)))
        my_numbers = set(map(int, re.findall(r"\d+", my_numbers_str)))
        winners = my_numbers.intersection(winning_numbers)
        for w in range(1, len(winners) + 1):
            cards[i + 1 + w] += 1 * (cards[i + 1])

    return sum(cards.values())


if __name__ == "__main__":
    print(part_a())
    print(part_b())
