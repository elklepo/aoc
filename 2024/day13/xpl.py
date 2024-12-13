import re


def solve_and_sum(cnt, prize_offset):
    s = 0
    for m in (list(map(int, re.findall(r'\d+', m))) for m in cnt.split('\n\n')):
        xa, ya, xb, yb, x, y = m
        x, y = x + prize_offset, y + prize_offset
        a = (yb * x - xb * y) / (xa * yb - xb * ya)
        b = (x - xa * a) / xb
        if a.is_integer() and b.is_integer():
            s += a * 3 + b
    return s


def task1(cnt):
    print(solve_and_sum(cnt, 0))


def task2(cnt):
    print(solve_and_sum(cnt, 10000000000000))
