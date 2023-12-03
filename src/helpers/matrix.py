

def neighbours_grid(point, x_len, y_len, diagonal=False):
    x, y = point
    return [
        (x + dx, y + dy)
        for dx, dy in _get_kernel(diagonal)
        if 0 <= (x + dx) <= x_len - 1 and 0 <= (y + dy) <= y_len - 1
    ]


def _get_kernel(diagonal):
    if diagonal:
        return [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    return [(0, 1), (0, -1), (1, 0), (-1, 0)]
