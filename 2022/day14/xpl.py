def _parse_lines(lines):
    rock_lines = []
    for l in lines:
        points = l.split(' -> ')
        for idx in range(len(points) - 1):
            x, y = (int(p) for p in points[idx].split(','))
            nx, ny = (int(p) for p in points[idx+1].split(','))
            rock_lines.append(((y, x), (ny, nx)))
    return rock_lines


def _init_grid(rock_lines):
    max_y = max(cord[0] for line in rock_lines for cord in line)
    max_x = max(cord[1] for line in rock_lines for cord in line)

    arr = [['.' for _ in range(max_x + 2)] for _ in range(max_y + 1)]
    for (sy, sx), (dy, dx) in rock_lines:
        vec_y = 0 if dy == sy else 1 if dy > sy else -1
        vec_x = 0 if dx == sx else 1 if dx > sx else -1
        x, y = sx, sy
        while not (x == dx and y == dy):
            arr[y][x] = '#'
            x += vec_x
            y += vec_y
        arr[y][x] = '#'
    return arr


def _emulate_sand_fall(grid):
    sand_units = 0
    while grid[0][500] == '.':
        y, x = (0, 500)
        while y < len(grid) - 1:
            for vec_y, vec_x in [(1, 0), (1, -1), (1, 1)]:
                if grid[y + vec_y][x + vec_x] == '.':
                    y += vec_y
                    x += vec_x
                    break
            else:
                # sand can't move
                grid[y][x] = 'o'
                sand_units += 1
                break
        else:
            # infinite fall
            break
    return sand_units


def task1(cnt):
    rock_lines = _parse_lines(cnt.splitlines())

    grid = _init_grid(rock_lines)

    print(_emulate_sand_fall(grid))


def task2(cnt):
    rock_lines = _parse_lines(cnt.splitlines())
    max_y = max(cord[0] for line in rock_lines for cord in line)
    max_x = max(cord[1] for line in rock_lines for cord in line)
    rock_lines.append(((max_y + 2, 0), (max_y + 2, max_x + max_y)))

    grid = _init_grid(rock_lines)

    print(_emulate_sand_fall(grid))
