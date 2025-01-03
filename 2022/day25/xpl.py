DEC_TO_SNAFU = {
    '4': '2',
    '3': '1',
    '2': '0',
    '1': '-',
    '0': '='
}
SNAFU_TO_DEC = {v: k for k, v in DEC_TO_SNAFU.items()}

def to_snafu(n):
    i = 0
    while 5**i < n:
        n += 2 * 5 ** i
        i+=1
    s = ""
    while n:
        s = str(n % 5) + s
        n //= 5
    return ''.join(DEC_TO_SNAFU[c] for c in s)


def task1(cnt):
    s = sum(sum((int(SNAFU_TO_DEC[c]) - 2) * 5**i for i, c in enumerate(l[::-1])) for l in cnt.splitlines())
    print(to_snafu(s))