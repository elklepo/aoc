from itertools import count
from collections import defaultdict, deque


def simulate(cnt, task1_rules):
    grid = {
        y + x * 1j
        for y, l in enumerate(cnt.splitlines())
        for x, c in enumerate(l)
        if c == '#'
    }
    prio = deque([-1, 1, -1j, 1j])

    for i in count(start=1):
        prop = defaultdict(list)

        for m in grid:
            if all(m + p not in grid and m + p + p * 1j not in grid for p in prio):
                continue
            for p in prio:
                if all(m + p + p * x not in grid for x in [-1j, 0, 1j]):
                    prop[m + p].append(m)
                    break

        prio.rotate(-1)

        for m in prop:
            if len(prop[m]) == 1:
                grid.add(m)
                grid.remove(prop[m][0])

        if task1_rules and i == 10:
            v = max(int(c.real) for c in grid) - min(int(c.real) for c in grid) + 1
            h = max(int(c.imag) for c in grid) - min(int(c.imag) for c in grid) + 1
            return v * h - len(grid)
        if not task1_rules and len(prop) == 0:
            return i


def task1(cnt):
    print(simulate(cnt, task1_rules=True))


def task2(cnt):
    print(simulate(cnt, task1_rules=False))
