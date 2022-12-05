import string


scoring = {
    c: i + 1
    for i, c
    in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}


def task1(cnt):
    bags = [(s[:len(s)//2], s[len(s)//2:]) for s in cnt.splitlines()]

    commons = [(set(h1) & set(h2)).pop() for h1, h2 in bags]

    print(sum(scoring[c] for c in commons))


def task2(cnt):
    bags = cnt.splitlines()

    groups = [bags[i:i + 3] for i in range(0, len(bags), 3)]

    labels = [(set(b1) & set(b2) & set(b3)).pop() for b1, b2, b3 in groups]

    print(sum(scoring[l] for l in labels))
