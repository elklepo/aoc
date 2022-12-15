import re
from z3 import *


def _parse_pairs(lines):
    pat = r'Sensor at x=([0-9-]+), y=([0-9-]+): closest beacon is at x=([0-9-]+), y=([0-9-]+)'.strip()
    pairs = []
    for m in lines:
        sx, sy, bx, by = (int(p) for p in re.search(pat, m).groups())
        pairs.append(((sy, sx), (by, bx)))
    return pairs


def task1(cnt):
    # very elegant way to detect sample input (input0)
    if cnt.startswith('Sensor at x=2, y=18: closest beacon is at x=-2, y=15'):
        y = 10
    else:
        y = 2000000

    pairs = _parse_pairs(cnt.splitlines())

    min_x, max_x = float('inf'), float('-inf')
    for (sy, sx), (by, bx) in pairs:
        max_range = abs(sy - by) + abs(sx - bx) + 1
        min_x = min(min_x, sx - max_range)
        max_x = max(max_x, sx + max_range)

    covered_ranges = []
    for (sy, sx), (by, bx) in pairs:
        vert_distance = abs(y - sy)
        max_range = abs(sy - by) + abs(sx - bx) + 1
        if vert_distance >= max_range:
            continue
        covered_ranges.append((sx - (max_range - vert_distance - 1), sx + (max_range - vert_distance - 1)))

    # merge the ranges
    while True:
        for i, j in ((i, j) for i in range(len(covered_ranges) - 1) for j in range(i + 1, len(covered_ranges))):
            min_1, max_1 = covered_ranges[i]
            min_2, max_2 = covered_ranges[j]
            if min_1 <= min_2 <= max_1 or min_2 <= min_1 <= max_2:
                set_1 = covered_ranges.pop(i)
                set_2 = covered_ranges.pop(j - 1)
                covered_ranges.append((min(set_1[0], set_2[0]), max(set_1[1], set_2[1])))
                break
        else:
            break

    total = sum(lx <= x <= hx for lx, hx in covered_ranges for x in range(min_x, max_x + 1))
    total -= sum(sensor_y == y for sensor_y, _ in set(p[0] for p in pairs))
    total -= sum(beacon_y == y for beacon_y, _ in set(p[1] for p in pairs))
    print(total)


def task2(cnt):
    # very elegant way detect to sample input (input0)
    if cnt.startswith('Sensor at x=2, y=18: closest beacon is at x=-2, y=15'):
        dim = 20
    else:
        dim = 4000000

    pairs = _parse_pairs(cnt.splitlines())

    def _z3_abs(n):
        return If(n >= 0, n, -n)

    solver = Solver()
    y = Int("y")
    x = Int("x")

    solver.add(And(x >= 0, x <= dim), y >= 0, y <= dim)

    for (sy, sx), (by, bx) in pairs:
        max_range = abs(sy - by) + abs(sx - bx)
        solver.add(_z3_abs(y - sy) + _z3_abs(x - sx) > max_range)

    solver.check()
    print(solver.model()[y].as_long() + 4000000 * solver.model()[x].as_long())

