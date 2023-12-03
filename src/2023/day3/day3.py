import re
from collections import defaultdict
from functools import reduce

from src.helpers import file_parser
from src.helpers import matrix


data = file_parser.file_as_line_list(2023, 3)
x_len = len(data[0])
y_len = len(data)


def part_a():
    numbers = find_numbers(data)

    part_numbers = []
    for y, numbers_on_line in numbers.items():
        for num, start, end in numbers_on_line:
            neighbours = set()
            for x in range(start, end):
                neighbours.update(set(matrix.neighbours_grid((x, y), x_len, y_len, diagonal=True)))

            for nx, ny in neighbours:
                if data[ny][nx] != "." and not data[ny][nx].isnumeric():
                    part_numbers.append(num)

    return sum(part_numbers)


def part_b():
    numbers = find_numbers(data)
    possible_gears = find_possible_gears(data)

    gear_ratios = []
    for possible_gear in possible_gears:
        gear_numbers = set()
        for nx, ny in matrix.neighbours_grid(possible_gear, x_len, y_len, diagonal=True):
            if data[ny][nx].isnumeric():
                for num, start, end in numbers[ny]:
                    if start <= nx < end:
                        gear_numbers.add(num)
                        break

        if len(gear_numbers) == 2:
            gear_ratios.append(reduce(lambda n, m: n * m, gear_numbers))

    return sum(gear_ratios)


def find_numbers(engine):
    number_spans: dict[int, list] = defaultdict(list)
    for i, line in enumerate(engine):
        for match in re.finditer(r"\d+", line):
            number_spans[i].append((int(match.group()), *match.span()))

    return number_spans


def find_possible_gears(engine):
    return [
        (x, y)
        for y, line in enumerate(engine)
        for x, symbol in enumerate(line)
        if symbol == "*"
    ]


if __name__ == "__main__":
    print(part_a())
    print(part_b())
