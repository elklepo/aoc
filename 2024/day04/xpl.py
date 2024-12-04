def parse_cnt(cnt):
    return cnt.splitlines()


def is_word(word, arr, y, x, dir_y, dir_x):
    for i in range(len(word)):
        n_y, n_x = y + i * dir_y, x + i * dir_x
        if not (0 <= n_y < len(arr)):
            break
        if not (0 <= n_x < len(arr[0])):
            break
        if arr[n_y][n_x] != word[i]:
            break
    else:
        return True
    return False


def task1(cnt):
    rows = parse_cnt(cnt)
    s = 0
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            s += sum(int(is_word('XMAS', rows, y, x, dir_y, dir_x))
                     for dir_y in [-1, 0, 1] for dir_x in [-1, 0, 1]
                     if not 0 == dir_y == dir_x)
    print(s)


def task2(cnt):
    rows = parse_cnt(cnt)
    s = 0
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if (is_word('MAS', rows, y, x, 1, 1) or is_word('SAM', rows, y, x, 1, 1)) \
                    and (is_word('MAS', rows, y, x + 2, 1, -1) or is_word('SAM', rows, y, x + 2, 1, -1)):
                s += 1
    print(s)
