from collections import Counter


def parse_cnt(cnt):
    list_a = []
    list_b = []
    for line in cnt.splitlines():
        n_a, n_b = line.split()
        list_a.append(int(n_a))
        list_b.append(int(n_b))
    return list_a, list_b


def task1(cnt):
    list_a, list_b = parse_cnt(cnt)
    print(sum(abs(a - b) for a, b in zip(sorted(list_a), sorted(list_b))))


def task2(cnt):
    list_a, list_b = parse_cnt(cnt)
    list_b_counter = Counter(list_b)
    print(sum(a * list_b_counter[a] for a in list_a))