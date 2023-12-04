from src.helpers import file_parser
import re

numbers_on_line = r"\d"
numbers_on_line_w_text = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
string_to_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part_a():
    numbers = [
        merge_numbers(*re.findall(numbers_on_line, line))
        for line in file_parser.file_as_line_list(year=2023, day=1)
    ]
    return sum(numbers)


def part_b():
    numbers = [
        merge_numbers(*re.findall(numbers_on_line_w_text, line))
        for line in file_parser.file_as_line_list(year=2023, day=1)
    ]
    return sum(numbers)


def merge_numbers(*numbers):
    x = string_to_number.get(numbers[0], numbers[0])
    y = string_to_number.get(numbers[-1], numbers[-1])

    return int(x) * 10 + int(y)


if __name__ == "__main__":
    print(part_a())
    print(part_b())
