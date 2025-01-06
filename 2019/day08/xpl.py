from collections import Counter
from itertools import batched, dropwhile


def task1(cnt):
    w, h = 25, 6
    layers = list(batched(cnt, w * h))
    pick = min(layers, key = lambda l: Counter(l)['0'])
    print(pick.count('1') * pick.count('2'))


def task2(cnt):
    w, h = 25, 6
    layers = list(batched(cnt, w * h))
    image = [next(dropwhile(lambda p: p == '2', (layers[i][j] for i in range(len(layers))))) for j in range(w * h)]
    print('\n'.join(''.join({'0': '  ', '1': '##'}[c] for c in l) for l in batched(image, w)))