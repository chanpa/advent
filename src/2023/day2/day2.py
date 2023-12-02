from collections import defaultdict
from functools import reduce
from src.helpers import file_parser


def part_a():
    data = file_parser.file_as_line_list(2023, 2)
    games = parse_cubes(data)

    limits = [("red", 12), ("green", 13), ("blue", 14)]
    invalid_games = set()
    for game_id, cubes in games.items():
        for color, limit in limits:
            if cubes[color] > limit:
                invalid_games.add(int(game_id))
                break

    all_game_ids = set(int(game_id) for game_id in games.keys())
    valid_games = all_game_ids - invalid_games

    return sum(valid_games)


def part_b():
    data = file_parser.file_as_line_list(2023, 2)
    games = parse_cubes(data)
    cube_powers = []
    for cubes in games.values():
        cube_powers.append(reduce(lambda x, y: x * y, cubes.values()))
    return sum(cube_powers)


def parse_cubes(data):
    games = defaultdict(lambda: defaultdict(int))
    for line in data:
        game, info = line.split(": ")
        _, game_id = game.split(" ")
        cube_sets = info.split("; ")
        for cube_set in cube_sets:
            for cube in cube_set.split(", "):
                num, color = cube.split(" ")
                if int(num) > games[game_id][color.strip()]:
                    games[game_id][color.strip()] = int(num)
    return games


if __name__ == "__main__":
    print(part_a())
    print(part_b())
