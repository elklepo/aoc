import re
import math


class Monkey:
    def __init__(self, idx, items, mod_operation, mod_operand, test, if_true, if_false):
        self.idx = idx
        self.items = items
        self.mod_operation = mod_operation
        self.mod_operand = mod_operand
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0
        self.lcm = 0

    def do_round(self, is_boring):
        for i in self.items:
            self.inspected += 1

            operand = i if self.mod_operand == 'old' else int(self.mod_operand)
            if self.mod_operation == '+':
                worry_level = i + operand
            else:  # self.mod_operation == '*':
                worry_level = i * operand

            if is_boring:
                worry_level //= 3

            worry_level %= self.lcm

            if worry_level % self.test:
                self.if_false.items.append(worry_level)
            else:
                self.if_true.items.append(worry_level)

        self.items = []


def _parse_monkeys(raw_monkeys):
    pat = r'''
Monkey ([0-9]+):
  Starting items: ([0-9, ]+)
  Operation: new = old (\+|\*) (old|[0-9]*)
  Test: divisible by ([0-9]+)
    If true: throw to monkey ([0-9]+)
    If false: throw to monkey ([0-9]+)
'''.strip()
    monkeys = []
    for m in raw_monkeys:
        idx, items, operation, operand, test, if_true, if_false = re.search(pat, m).groups()
        monkeys.append(
            Monkey(
                idx=int(idx),
                items=[int(i) for i in items.split(',')],
                mod_operation=operation,
                mod_operand=operand,
                test=int(test),
                if_true=int(if_true),
                if_false=int(if_false)))

    lcm = math.lcm(*[m.test for m in monkeys])

    for m in monkeys:
        m.if_true = monkeys[m.if_true]
        m.if_false = monkeys[m.if_false]
        m.lcm = lcm

    return monkeys


def task1(cnt):
    monkeys = _parse_monkeys(cnt.split('\n\n'))
    for _ in range(20):
        for m in monkeys:
            m.do_round(is_boring=True)
    p2, p1 = sorted(m.inspected for m in monkeys)[-2:]
    print(p2*p1)


def task2(cnt):
    monkeys = _parse_monkeys(cnt.split('\n\n'))
    for _ in range(10000):
        for m in monkeys:
            m.do_round(is_boring=False)
    p2, p1 = sorted(m.inspected for m in monkeys)[-2:]
    print(p2*p1)