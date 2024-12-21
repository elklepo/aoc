import math
from functools import cache


NUMPAD = {
    '7': 0,
    '8': 1j,
    '9': 2j,
    '4': 1,
    '5': (1+1j),
    '6': (1+2j),
    '1': 2,
    '2': (2+1j),
    '3': (2+2j),
    '0': (3+1j),
    'A': (3+2j)
}

DIRPAD = {
    '^': 1j,
    'A': 2j,
    '<': 1,
    'v': (1+1j),
    '>': (1+2j)
}


def best_path(start, end, robots, pad):
    ret = math.inf
    todo = [(start, "")]
    while todo:
        p, path = todo.pop(0)
        if p == end:
            ret = min(ret, best_robot(path + "A", robots - 1))
        elif p in pad.values():
            if p.imag < end.imag: todo.append((p+1j, path + '>'))
            if p.imag > end.imag: todo.append((p-1j, path + '<'))
            if p.real < end.real: todo.append((p+1, path + 'v'))
            if p.real > end.real: todo.append((p-1, path + '^'))
    return ret


@cache
def best_robot(path, robots):
    if robots == 0:
        return len(path)

    start = DIRPAD['A']
    return sum(best_path(start, start := DIRPAD[n], robots, DIRPAD) for n in path)


def task1(cnt):
    start = NUMPAD['A']
    print(sum(sum(best_path(start, start := NUMPAD[n], 3, NUMPAD) for n in l) * int(l[:-1]) for l in cnt.splitlines()))


def task2(cnt):
    start = NUMPAD['A']
    print(sum(sum(best_path(start, start := NUMPAD[n], 26, NUMPAD) for n in l) * int(l[:-1]) for l in cnt.splitlines()))