

def neighbours_grid(point, x_max, y_max, diagonal=False):
    x, y = point
    return [
        (x + dx, y + dy)
        for dx, dy in _get_kernel(diagonal)
        if 0 <= (x + dx) <= x_max and 0 <= (y + dy) <= y_max
    ]


def _get_kernel(diagonal):
    if diagonal:
        return [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    return [(0, 1), (0, -1), (1, 0), (-1, 0)]
