import re
import math


def recalculate_state_task1(grid, pos, dir):
    n_pos = pos + dir
    if n_pos in grid:
        return n_pos, dir

    match dir:
        case 1:   return min((c for c in grid if c.imag == pos.imag), key=lambda c: c.real), dir
        case -1:  return max((c for c in grid if c.imag == pos.imag), key=lambda c: c.real), dir
        case 1j:  return min((c for c in grid if c.real == pos.real), key=lambda c: c.imag), dir
        case -1j: return max((c for c in grid if c.real == pos.real), key=lambda c: c.imag), dir


def recalculate_state_task2(grid, pos, dir):
    n_pos = pos + dir
    if n_pos in grid:
        return n_pos, dir

    dim = int(math.sqrt(len(grid) // 6))
    sec_y, sec_x = (int(pos.real) // dim, int(pos.imag) // dim)
    rel_y, rel_x = (int(pos.real) % dim, int(pos.imag) % dim)

    # That was a lot of time with pen and paper...
    match (sec_y, sec_x), dir:
        case (0, 1), -1:  y, x, dir = 3 * dim + rel_x, 0 * dim + 0, 1j
        case (0, 1), -1j: y, x, dir = 2 * dim + dim - rel_y - 1, 0 * dim + 0, 1j
        case (0, 2), 1:   y, x, dir = 1 * dim + rel_x, 1 * dim + dim - 1, -1j
        case (0, 2), -1:  y, x, dir = 3 * dim + dim - 1, 0 * dim + rel_x, -1
        case (0, 2), 1j:  y, x, dir = 2 * dim + dim - rel_y - 1, 1 * dim + dim - 1, -1j
        case (1, 1), -1j: y, x, dir = 2 * dim + 0, 0 * dim + rel_y, 1
        case (1, 1), 1j:  y, x, dir = 0 * dim + dim - 1, 2 * dim + rel_y, -1
        case (2, 0), -1:  y, x, dir = 1 * dim + rel_x, 1 * dim + 0, 1j
        case (2, 0), -1j: y, x, dir = 0 * dim + dim - rel_y - 1, 1 * dim + 0, 1j
        case (2, 1), 1:   y, x, dir = 3 * dim + rel_x, 0 * dim + dim - 1, -1j
        case (2, 1), 1j:  y, x, dir = 0 * dim + dim - rel_y - 1, 2 * dim + dim - 1, -1j
        case (3, 0), 1:   y, x, dir = 0 * dim + 0, 2 * dim + rel_x, 1
        case (3, 0), -1j: y, x, dir = 0 * dim + 0, 1 * dim + rel_y, 1
        case (3, 0), 1j:  y, x, dir = 2 * dim + dim - 1, 1 * dim + rel_y, -1
    return y + x * 1j, dir


def simulate(cnt, recalculate_state):
    grid, moves = cnt.split('\n\n')
    grid = {
        (y + x * 1j): c
        for y, l in enumerate(grid.splitlines())
        for x, c in enumerate(l)
        if c != ' '
    }
    pos = min((c for c in grid if c.real == 0), key=lambda c: c.imag)
    dir = 1j
    q = re.findall(re.compile(r"\d+|[LR]"), moves)[::-1]
    while True:
        dist = int(q.pop())
        for _ in range(dist):
            n_pos, n_dir = recalculate_state(grid, pos, dir)
            if grid[n_pos] == '#':
                break
            pos, dir = n_pos, n_dir
        if not q:
            break
        dir *= -1j if q.pop() == 'R' else 1j
    return pos, dir


def task1(cnt):
    pos, dir = simulate(cnt, recalculate_state_task1)
    print(int(pos.real + 1) * 1000 + int(pos.imag + 1) * 4 + [1j, 1, -1j, -1].index(dir))


def task2(cnt):
    pos, dir = simulate(cnt, recalculate_state_task2)
    print(int(pos.real + 1) * 1000 + int(pos.imag + 1) * 4 + [1j, 1, -1j, -1].index(dir))
