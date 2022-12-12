def _is_one_range_in_another(r1, r2):
    lr1, ur1 = r1
    lr2, ur2 = r2
    return (lr2 <= lr1 <= ur1 <= ur2) or (lr1 <= lr2 <= ur2 <= ur1)


def _do_ranges_overlap(r1, r2):
    lr1, ur1 = r1
    lr2, ur2 = r2
    return _is_one_range_in_another(r1, r2) or (lr2 <= lr1 <= ur2 <= ur1) or (lr1 <= lr2 <= ur1 <= ur2)


def task1(cnt):
    pairs = []
    for line in cnt.splitlines():
        r1, r2 = line.split(',')
        lr1, ur1 = r1.split('-')
        lr2, ur2 = r2.split('-')
        r1 = (int(lr1), int(ur1))
        r2 = (int(lr2), int(ur2))
        pairs.append((r1, r2))

    print(sum(_is_one_range_in_another(r1, r2) for r1, r2 in pairs))


def task2(cnt):
    pairs = []
    for line in cnt.splitlines():
        r1, r2 = line.split(',')
        lr1, ur1 = r1.split('-')
        lr2, ur2 = r2.split('-')
        r1 = (int(lr1), int(ur1))
        r2 = (int(lr2), int(ur2))
        pairs.append((r1, r2))

    print(sum(_do_ranges_overlap(r1, r2) for r1, r2 in pairs))