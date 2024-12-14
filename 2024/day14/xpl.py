import re
import numpy as np
from collections import defaultdict
from dataclasses import dataclass
from scipy.stats import entropy

X, Y = 101, 103

@dataclass
class Robot:
   px: int
   py: int
   vx: int
   vy: int


def parse_cnt(cnt):
    return [Robot(px, py, vx, vy) for px, py, vx, vy
            in ((map(int, re.findall(r'-?\d+', r))) for r in cnt.splitlines())]


def task1(cnt):
    m = defaultdict(int)
    robots = parse_cnt(cnt)
    for r in robots:
        r.py, r.px = (r.py + r.vy * 100) % Y, (r.px + r.vx * 100) % X
        m[r.py, r.px] += 1

    q1 = sum(m[y, x] for y in range(Y//2) for x in range(X//2))
    q2 = sum(m[y, x] for y in range(Y//2) for x in range(X//2 + 1, X))
    q3 = sum(m[y, x] for y in range(Y//2 + 1, Y) for x in range(X//2))
    q4 = sum(m[y, x] for y in range(Y//2 + 1, Y) for x in range(X//2 + 1, X))
    print(q1 * q2 * q3 * q4)


def task2(cnt):
    robots = parse_cnt(cnt)
    max_entropy, max_entropy_idx = 0, 0

    for i in range(1, 100000):
        m = defaultdict(int)
        for r in robots:
            r.py, r.px = (r.py + r.vy) % Y, (r.px + r.vx) % X
            m[r.py, r.px] += 1

        if (e := entropy(np.array([m[y, x] for y in range(Y) for x in range(X)]))) > max_entropy:
            max_entropy, max_entropy_idx = e, i
            print(max_entropy_idx)