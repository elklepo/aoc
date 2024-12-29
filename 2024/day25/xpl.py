from itertools import combinations


def task1(cnt):
    codes = [{i for i, c in enumerate(g) if c == '#'} for g in cnt.split('\n\n')]
    print(sum(not k & l for k, l in combinations(codes, 2)))
