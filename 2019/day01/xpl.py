def task1(cnt):
    print(sum(m // 3 - 2 for m in map(int, cnt.splitlines())))


def task2(cnt):
    s = 0
    for p in map(int, cnt.splitlines()):
         while (p := p // 3 - 2) > 0:
             s += p
    print(s)