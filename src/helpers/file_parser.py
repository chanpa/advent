from pathlib import Path


def file_as_line_list(year, day, test=None):
    base_path = Path(__file__).parent.parent / f"{year}/day{day}"
    match test:
        case "a": path = Path(base_path) / "test_a.txt"
        case "b": path = Path(base_path) / "test_b.txt"
        case _: path = Path(base_path) / "input.txt"
    return [line.strip() for line in open(path)]
