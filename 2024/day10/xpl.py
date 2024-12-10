from collections import defaultdict


def parse_cnt(cnt):
    return {
        (y+x*1j): int(c)
        for y, l in enumerate(cnt.splitlines())
        for x, c in enumerate(l)
    }


def build(m, c, v):
    if m[c] == 9:
        v[c] = [{c}]
    else:
        for vector in (0+1j, 1, 0-1j, -1):
            if (nc := c + vector) in m and m[nc] == m[c] + 1:
                if nc not in v:
                    build(m, nc, v)
                v[c] |= {frozenset({c} | x) for x in v[nc]}


def task1(cnt):
    m = parse_cnt(cnt)
    v = defaultdict(set)
    for c in m:
        build(m, c, v)
    print(sum(len({next(filter(lambda e: m[e] == 9, x)) for x in v[c]}) for c in m if m[c] == 0))


def task2(cnt):
    m = parse_cnt(cnt)
    v = defaultdict(set)
    for c in m:
        build(m, c, v)
    print(sum(len(v[c]) for c in m.keys() if m[c] == 0))
