from collections import defaultdict
from itertools import chain


def parse_cnt(cnt):
    return defaultdict(str) | {
        y+x*1j: c
        for y, l in enumerate(cnt.splitlines())
        for x, c in enumerate(l)
    }


def get_fences_cost(cnt, task2_rules):
    garden = parse_cnt(cnt)
    visited = set()
    cost = 0
    fences = defaultdict(list)
    for pos in list(garden.keys()):
        if pos in visited:
            continue
        q = [pos]
        size = 0
        while q:
            e = q.pop()
            if e in visited:
                continue
            visited.add(e)
            size += 1
            for v in (0+1j, 1, 0-1j, -1):
                if garden[e+v] == garden[e]:
                    q.append(e+v)
                    continue
                found = [ii for ii, fence in enumerate(fences[v])
                         if any(e == (elem + v * -1j) or e == (elem + v * 1j) for elem in fence)]
                if not found:
                    fences[v].append([e])
                elif len(found) == 1:
                    fences[v][found[0]].append(e)
                elif len(found) == 2:
                    fences[v][found[0]].extend(fences[v][found[1]] + [e])
                    del fences[v][found[1]]

        if task2_rules:
            cost += size * sum(len(xx) for _, xx in fences.items())
        else:
            cost += size * sum(len(list(chain.from_iterable(xx))) for _, xx in fences.items())
        fences.clear()

    return cost


def task1(cnt):
    print(get_fences_cost(cnt, False))


def task2(cnt):
    print(get_fences_cost(cnt, True))
