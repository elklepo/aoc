from collections import defaultdict
from itertools import combinations


def build_graph(cnt):
    g = defaultdict(set)
    for a, b in (l.split('-') for l in cnt.splitlines()):
        g[a].add(b)
        g[b].add(a)
    return g


def task1(cnt):
    g = build_graph(cnt)
    networks = {frozenset((e, a, b)) for e in g for a, b in combinations(g[e], 2) if a in g[b]}
    print(sum(any(e[0] == 't' for e in n) for n in networks))


def task2(cnt):
    g = build_graph(cnt)
    biggest = max((set(c) | {e}
                   for e in g
                   for i in range(len(g[e]), 1, -1)
                   for c in combinations(g[e], i)
                   if all(a in g[b] for a, b in combinations(c, 2))
                   ), key=len)
    print(','.join(sorted(biggest)))


