def task1(cnt):
    bags = [[int(item) for item in bag.split('\n')] for bag in cnt.split('\n\n')]

    cals = [sum(bag) for bag in bags]

    print(max(cals))


def task2(cnt):
    bags = [[int(item) for item in bag.split('\n')] for bag in cnt.split('\n\n')]

    cals = [sum(bag) for bag in bags]

    print(sum(sorted(cals)[-3:]))