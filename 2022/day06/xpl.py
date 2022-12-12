def task1(cnt):
    for i in range(3, len(cnt)):
        if len(set(cnt[i-4:i])) == 4:
            print(i)
            break


def task2(cnt):
    for i in range(3, len(cnt)):
        if len(set(cnt[i-14:i])) == 14:
            print(i)
            break
