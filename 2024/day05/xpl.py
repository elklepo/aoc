from functools import cmp_to_key


def parse_cnt(cnt):
    rules, updates = cnt.split('\n\n')
    rules = set(tuple(int(x) for x in rule.split('|')) for rule in rules.splitlines())
    updates = [[int(x) for x in update.split(',')] for update in updates.splitlines()]
    return rules, updates


def create_compare_func(rules):
    def compare(a, b):
        return -1 if (a, b) in rules else 1
    return compare


def task1(cnt):
    rules, updates = parse_cnt(cnt)
    print(sum(u[len(u) // 2] for u in updates if u == sorted(u, key=cmp_to_key(create_compare_func(rules)))))


def task2(cnt):
    rules, updates = parse_cnt(cnt)
    print(sum(s[len(s) // 2] for u in updates if (s := sorted(u, key=cmp_to_key(create_compare_func(rules)))) != u))

