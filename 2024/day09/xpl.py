def parse_cnt(cnt):
    disk, spaces, files = [], [], []
    for i, c in enumerate(cnt):
        if i % 2:
            spaces.append((int(c), len(disk)))
        else:
            files.append((int(i//2), int(c), len(disk)))
        disk += [-1 if i % 2 else int(i//2) for _ in range(int(c))]
    return disk, spaces, files


def task1(cnt):
    disk, _, _ = parse_cnt(cnt)
    fp, ep = 0, len(disk) - 1
    while True:
        while disk[fp] != -1:
            fp += 1
        while disk[ep] == -1:
            ep -= 1
        if fp >= ep:
            break
        disk[fp], disk[ep] = disk[ep], disk[fp]

    print(sum(disk[i] * i for i in range(len(disk)) if disk[i] > 0))


def task2(cnt):
    disk, spaces, files = parse_cnt(cnt)
    while files:
        fid, flen, fidx = files.pop()

        for i, (slen, sidx) in enumerate(spaces):
            if fidx < sidx:
                break
            if slen >= flen:
                disk[fidx:fidx + flen] = [-1] * flen
                disk[sidx:sidx + flen] = [fid] * flen
                if slen > flen:
                    spaces[i] = (slen - flen, sidx+flen)
                else:
                    spaces.pop(i)
                break
    print(sum(disk[i] * i for i in range(len(disk)) if disk[i] > 0))