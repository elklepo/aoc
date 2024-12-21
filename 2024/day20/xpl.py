from itertools import combinations


def solve(cnt, cheat_len):
    grid = {
        (y + x * 1j): c
        for y, l in enumerate(cnt.splitlines())
        for x, c in enumerate(l)
        if c != '#'
    }
    start, = (k for k in grid if grid[k] == 'S')
    end, = (k for k in grid if grid[k] == 'E')

    from_start = {start: 0}
    p = start
    while p != end:
        for n in (p + d for d in [1, -1, -1j, +1j]):
            if n in grid and n not in from_start:
                from_start[n] = from_start[p] + 1
                p = n
                break

    s = 0
    for (a, da), (b, db) in combinations(from_start.items(), 2):
        d = abs((a - b).real) + abs((a - b).imag)
        if d <= cheat_len and abs(db - da) - d >= 100: s += 1
    return s


def task1(cnt):
    print(solve(cnt, 2))


def task2(cnt):
    print(solve(cnt, 20))