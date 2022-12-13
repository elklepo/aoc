import ast
import functools


def _compare_items(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return 0 if l == r else -1 if l < r else 1
    if isinstance(l, list) and isinstance(r, int):
        r = [r]
    if isinstance(l, int) and isinstance(r, list):
        l = [l]
    for li, ri in zip(l, r):
        res = _compare_items(li, ri)
        if res != 0:
            return res
    return 0 if len(l) == len(r) else -1 if len(l) < len(r) else 1


def _parse_pairs(raw_pairs):
    return [(ast.literal_eval(p1), ast.literal_eval(p2)) for p1, p2 in (pair.split('\n') for pair in raw_pairs)]


def task1(cnt):
    pairs = _parse_pairs(cnt.split('\n\n'))
    print(sum(idx+1 for idx, pair in enumerate(pairs) if _compare_items(*pair) == -1))


def task2(cnt):
    pairs = _parse_pairs(cnt.split('\n\n'))
    all_packets = [packet for pair in pairs for packet in pair]

    control_packets = [[[2]], [[6]]]
    all_packets.extend(control_packets)

    sorted_packets = sorted(all_packets, key=functools.cmp_to_key(_compare_items))
    print((sorted_packets.index(control_packets[0]) + 1) * (sorted_packets.index(control_packets[1]) + 1))

