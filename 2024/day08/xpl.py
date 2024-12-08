from collections import defaultdict
from itertools import combinations, chain


def parse_cnt(cnt):
    m = defaultdict(list)
    for y, l in enumerate(cnt.splitlines()):
        for x, c in enumerate(l):
            m[c].append(y+x*1j)
    return m


def task1(cnt):
    m = parse_cnt(cnt)
    all_points = {p for p in chain.from_iterable(m.values())}
    del m['.']
    anti = set()
    for c, ant in m.items():
        for a, b in combinations(ant, 2):
            d = a - b
            if (a := a + d) in all_points:
                anti.add(a)
            if (b := b - d) in all_points:
                anti.add(b)
    print(len(anti))


def task2(cnt):
    m = parse_cnt(cnt)
    all_points = {p for p in chain.from_iterable(m.values())}
    del m['.']
    anti = set()
    for c, ant in m.items():
        for a, b in combinations(ant, 2):
            d = a - b
            while (a := a - d) in all_points:
                anti.add(a)
            while (b := b + d) in all_points:
                anti.add(b)
    print(len(anti))