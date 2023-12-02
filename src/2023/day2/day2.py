from collections import defaultdict
from functools import reduce
from src.helpers import file_parser


def part_a():
    data = file_parser.file_as_line_list(2023, 2)
    games = parse_cubes_new(data)

    limits = [("red", 12), ("green", 13), ("blue", 14)]
    invalid_games = set()
    for game_id, cubes in games.items():
        for color, limit in limits:
            if cubes[color] > limit:
                invalid_games.add(game_id)
                break

    return sum(games.keys() - invalid_games)


def part_b():
    data = file_parser.file_as_line_list(2023, 2)
    games = parse_cubes_new(data)

    cube_powers = []
    for cubes in games.values():
        cube_powers.append(reduce(lambda x, y: x * y, cubes.values()))

    return sum(cube_powers)


def parse_cubes(data):
    games: dict[int, dict] = defaultdict(lambda: defaultdict(int))
    for line in data:
        game, info = line.split(": ")
        game_id = int(game.split(" ")[-1])
        for cube_set in info.split("; "):
            for cube in cube_set.split(", "):
                num, color = cube.strip().split(" ")
                num = int(num)
                if num > games[game_id][color]:
                    games[game_id][color] = num
    return games


def parse_cubes_new(data):
    games: dict[int, dict] = defaultdict(lambda: defaultdict(int))
    for line in data:
        info = line.replace(",", "").replace(";", "").replace(":", "").strip().split(" ")
        game_id = int(info[1])
        for i in range(2, len(info[2:]) + 1, 2):
            num, color = int(info[i]), info[i + 1]
            if num > games[game_id][color]:
                games[game_id][color] = num
    return games


if __name__ == "__main__":
    print(part_a())
    print(part_b())
