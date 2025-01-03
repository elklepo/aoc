from collections import defaultdict, deque
from math import lcm


def get_path_len(white, cycle, start, end, start_time):
    seen = set()
    q = deque([(start, start_time)])
    while True:
        (y, x), r = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]:
            n = (y + dy, x + dx)
            if n == end:
                return r + 1
            if n in white and (r + 1) % cycle in white[n]:
                if (n, (r + 1) % cycle) not in seen:
                    seen.add((n, (r + 1) % cycle))
                    q.append((n, r + 1))

def solve(cnt, task2_rules):
    grid = defaultdict(list) | {
        (y, x): {'.': [], '^': [(-1, 0)], 'v': [(1, 0)], '<': [(0, -1)], '>': [(0, 1)]}[c][:]
        for y, l in enumerate(cnt.splitlines())
        for x, c in enumerate(l)
        if c != '#'
    }
    tmp = defaultdict(list)
    white = defaultdict(set)

    h, w = max(m[0] for m in grid) - 1, max(m[1] for m in grid)
    cycle = lcm(h, w)
    for i in range(lcm(h, w)):
        for y in range(1, h + 1):
            for x in range(1, w + 1):
                if not grid[(y, x)]:
                    white[(y, x)].add(i)
                for (dy, dx) in grid[(y, x)]:
                    tmp[((y + dy - 1) % h + 1, (x + dx - 1) % w  + 1)].append((dy, dx))
        grid, tmp = tmp, grid
        tmp.clear()

    start, end = (0,1), (h + 1, w)
    white[start] = white[end] = set(range(cycle))
    t = get_path_len(white, cycle, start, end, 0)
    if task2_rules:
        t = get_path_len(white, cycle, end, start, t)
        t = get_path_len(white, cycle, start, end, t)
    return t


def task1(cnt):
    print(solve(cnt, task2_rules=False))


def task2(cnt):
    print(solve(cnt, task2_rules=True))
