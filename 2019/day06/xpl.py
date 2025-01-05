import re
from itertools import accumulate, repeat, takewhile


class Node:
    def __init__(self, name):
        self.name = name
        self.orbits = None
        self.orbited_by = set()


def parse_nodes(cnt):
    node_names = set(re.split(r'[\n)]', cnt))
    nodes = {name: Node(name) for name in node_names}
    for c, o in (l.split(')') for l in cnt.splitlines()):
        nodes[c].orbited_by.add(nodes[o])
        nodes[o].orbits = nodes[c]
    return nodes


def task1(cnt):
    nodes = parse_nodes(cnt)
    def get_orbits(n):
        return 1 + get_orbits(n.orbits) if n.orbits is not None else 0
    print(sum(get_orbits(nodes[n]) for n in nodes))


def task2(cnt):
    nodes = parse_nodes(cnt)
    you_p = list(takewhile(lambda n: n is not None, accumulate(repeat(1), lambda n, _: n.orbits, initial=nodes['YOU'])))
    san_p = list(takewhile(lambda n: n is not None, accumulate(repeat(1), lambda n, _: n.orbits, initial=nodes['SAN'])))
    common = next(filter(set(san_p).__contains__, you_p))
    print(san_p.index(common) + you_p.index(common) - 2)