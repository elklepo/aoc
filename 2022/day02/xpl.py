def task1(cnt):
    results = {
        "A Y": 6 + 2,
        "A X": 3 + 1,
        "A Z": 0 + 3,
        "B Y": 3 + 2,
        "B X": 0 + 1,
        "B Z": 6 + 3,
        "C Y": 0 + 2,
        "C X": 6 + 1,
        "C Z": 3 + 3,
    }

    strats = cnt.splitlines()
    print(sum(results[s] for s in strats))


def task2(cnt):
    results = {
        "A Y": 1 + 3,
        "A X": 3 + 0,
        "A Z": 2 + 6,
        "B Y": 2 + 3,
        "B X": 1 + 0,
        "B Z": 3 + 6,
        "C Y": 3 + 3,
        "C X": 2 + 0,
        "C Z": 1 + 6,
    }

    strats = cnt.splitlines()
    print(sum(results[s] for s in strats))

