import re
from collections import defaultdict
from functools import cache
from z3 import *


@cache
def get_val(node):
    if node.const_val is not None:
        return node.const_val
    match node.op:
        case 'OR':
            return get_val(node.a) | get_val(node.b)
        case 'AND':
            return get_val(node.a) & get_val(node.b)
        case 'XOR':
            return get_val(node.a) ^ get_val(node.b)

class Node:
    def __init__(self):
        self.name = None
        self.op = None
        self.a = None
        self.b = None
        self.const_val = None


def task1_z3(cnt):
    s = Solver()
    x = BitVec('x', 45)
    y = BitVec('y', 45)
    z = BitVec('z', 46)

    def get_bitvec(n):
        vals = {'x': x, 'y': y, 'z': z}
        if n[0] in vals:
            return Extract(int(n[1:]), int(n[1:]), vals[n[0]])
        else:
            return BitVec(n, 1)

    defs, eqs = cnt.split('\n\n')
    for l in defs.splitlines():
        name, val = (v.strip() for v in l.split(':'))
        s.add(get_bitvec(name) == int(val))

    for l in eqs.splitlines():
        a, op, b, c = re.findall(r'\w+', l)
        a, b, c = get_bitvec(a), get_bitvec(b), get_bitvec(c)
        match op:
            case 'OR':
                s.add((a | b) == c)
            case 'AND':
                s.add((a & b) == c)
            case 'XOR':
                s.add((a ^ b) == c)
    if s.check() == sat:
        X, Y, Z = s.model()[x].as_long(), s.model()[y].as_long(), s.model()[z].as_long()
        print(Z)


def task1(cnt):
    nodes = defaultdict(Node)
    defs, ops = cnt.split('\n\n')
    for l in defs.splitlines():
        name, val = (v.strip() for v in l.split(':'))
        nodes[name].name = name
        nodes[name].const_val = int(val)
    for l in ops.splitlines():
        a, op, b, c = re.findall(r'\w+', l)
        nodes[c].name = c
        nodes[c].a = nodes[a]
        nodes[c].b = nodes[b]
        nodes[c].op = op
    print(sum((get_val(nodes[label]) << int(label[1:])) for label in sorted(nodes.keys()) if label[0] == 'z'))

def task2(cnt):
    _, ops = cnt.split('\n\n')
    ops = [re.findall(r'\w+', l) for l in ops.splitlines()]
    max_z = max(res for _, _, _, res in ops if res[0] == 'z')

    wrong = set()
    for a, op, b, r in ops:
        if op != 'XOR' and r[0] == 'z' and r != max_z:
            wrong.add(r)

        if op == 'XOR' and all(o[0] not in 'xyz' for o in [a, b, r]):
            wrong.add(r)

        if op == 'AND' and 'x00' not in [a, b] and any(sop != "OR" and r in [sa, sb] for sa, sop, sb, sr in ops):
            wrong.add(r)

        if op == "XOR" and any(sop == "OR" and r in [sa, sb] for sa, sop, sb, sr in ops):
            wrong.add(r)

    print(",".join(sorted(wrong)))