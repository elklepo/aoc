from itertools import cycle


def parse_cnt(cnt):
    return {(y, x): c
            for y, l in enumerate(cnt.splitlines())
            for x, c in enumerate(l)}


def get_seen(m, start):
    dir_iter = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    d = next(dir_iter)
    p = start
    seen = set()
    while p in m and (p, d) not in seen:
        seen.add((p, d))
        while m.get((p[0] + d[0], p[1] + d[1])) == '#':
            d = next(dir_iter)
        p = (p[0] + d[0], p[1] + d[1])
    return seen, p in m


def task1(cnt):
    m = parse_cnt(cnt)
    start = next((k for k in m if m[k] == '^'), None)
    seen, _ = get_seen(m, start)
    print(len(set(pos for pos, _ in seen)))


def task2(cnt):
    m = parse_cnt(cnt)
    start = next((k for k in m if m[k] == '^'), None)
    seen, _ = get_seen(m, start)
    print(sum(get_seen(m | {pos: '#'}, start)[1] for pos in set(pos for pos, _ in seen)))
