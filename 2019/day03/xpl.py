def translate(inst):
    p = 0
    s = 0
    seen = dict()
    for x in inst.split(','):
        d, c = {'U': -1, 'D': 1, 'L': -1j, 'R': 1j}[x[0]], int(x[1:])
        for i in range(c):
            s += 1
            p += d
            if p not in seen:
                seen[p] = s
    return seen

def task1(cnt):
    a = translate(cnt.splitlines()[0])
    b = translate(cnt.splitlines()[1])
    print(int(min(abs(k.real) + abs(k.imag) for k in a.keys() & b.keys())))


def task2(cnt):
    a = translate(cnt.splitlines()[0])
    b = translate(cnt.splitlines()[1])
    print(min(a[k] + b[k] for k in a.keys() & b.keys()))