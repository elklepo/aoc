import re
from functools import reduce


def parse_cnt(cnt):
    return [(int(eq), list(map(int, nums))) for eq, *nums in (re.findall(r'\d+', l) for l in cnt.splitlines())]


def task1(cnt):
    equations = parse_cnt(cnt)

    def reduce_routine(res, n):
        return [op(r, n) for r in res for op in (lambda a, b: a+b, lambda a, b: a*b)]

    print(sum((eq * (eq in reduce(reduce_routine, [[nums[0]]] + nums[1:])) for eq, nums in equations)))


def task2(cnt):
    equations = parse_cnt(cnt)

    def reduce_routine(res, n):
        return [op(r, n) for r in res for op in (lambda a, b: a+b, lambda a, b: a*b, lambda a, b: int(str(a)+str(b)))]

    print(sum((eq * (eq in reduce(reduce_routine, [[nums[0]]] + nums[1:])) for eq, nums in equations)))
