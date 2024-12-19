from collections import defaultdict
from functools import cache


class Node:
    def __init__(self):
        self.neigh = defaultdict(lambda: None)
        self.val = None

def parse_cnt(cnt):
    head = Node()
    towels, patterns = cnt.split('\n\n')
    for towel in towels.split(', '):
        p = head
        for c in towel:
            if not p.neigh[c]:
                p.neigh[c] = Node()
            p = p.neigh[c]
        p.val = towel
    return head, patterns.splitlines()


@cache
def count(head, word):
    if word == '':
        return 1
    p, s = head, 0
    for c in word:
        if (p := p.neigh[c]) is None:
            break
        if p.val is not None:
            s += count(head, word[len(p.val):])
    return s


def task1(cnt):
    head, patterns = parse_cnt(cnt)
    print(sum(count(head, p) > 0 for p in patterns))


def task2(cnt):
    head, patterns = parse_cnt(cnt)
    print(sum(count(head, p) for p in patterns))