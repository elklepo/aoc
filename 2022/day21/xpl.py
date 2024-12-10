from z3 import *
import re


def solve(cnt, task2_rules):
    as_pattern = re.compile(r"([a-z]{,4}): (\d{,4})")
    eq_pattern = re.compile(r"([a-z]{,4}): ([a-z]{,4}) ([+\-*/]) ([a-z]{,4})")
    s = Solver()
    for l in cnt.splitlines():
        if cap := re.fullmatch(as_pattern, l):
            var, val = cap.groups()
            if task2_rules and var == 'humn':
                continue
            s.add(Int(var) == int(val))
        elif cap := re.fullmatch(eq_pattern, l):
            var, op1, o, op2 = cap.groups()
            if task2_rules and var == 'root':
                s.add(Int(op1) == Int(op2))
                continue
            match o:
                case '+':
                    s.add(Int(var) == Int(op1) + Int(op2))
                case '-':
                    s.add(Int(var) == Int(op1) - Int(op2))
                case '*':
                    s.add(Int(var) == Int(op1) * Int(op2))
                case '/':
                    s.add(Int(var) == Int(op1) / Int(op2))
    if s.check() == sat:
        return s.model()[Int('humn' if task2_rules else 'root')]


def task1(cnt):
    print(solve(cnt, False))


def task2(cnt):
    print(solve(cnt, True))