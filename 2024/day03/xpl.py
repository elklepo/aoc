import re
from queue import PriorityQueue


def task1(cnt):
    p = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    print(sum(int(x) * int(y) for x, y in re.findall(p, cnt)))


def task2(cnt):
    pq = PriorityQueue()
    for m in re.finditer(re.compile(r"mul\((\d{1,3}),(\d{1,3})\)"), cnt):
        pq.put((m.start(), (int(m.group(1)), int(m.group(2)))))

    for m in re.finditer(re.compile(r"do\(\)"), cnt):
        pq.put((m.start(), True))

    for m in re.finditer(re.compile(r"don't\(\)"), cnt):
        pq.put((m.start(), False))

    s = 0
    enabled = True
    while not pq.empty():
        _, val = pq.get()
        if isinstance(val, bool):
            enabled = val
        elif enabled:
            s += val[0] * val[1]
    print(s)
