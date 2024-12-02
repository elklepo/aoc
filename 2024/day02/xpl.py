def parse_cnt(cnt):
    return [[int(l) for l in r.split()] for r in cnt.splitlines()]


def get_faulty_level_index(report):
    prev_diff = report[1] - report[0]
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if not 1 <= abs(diff) <= 3:
            return i
        if prev_diff * diff < 0:
            return i
        prev_diff = diff
    else:
        return None


def task1(cnt):
    safe_reports = 0
    reports = parse_cnt(cnt)
    for report in reports:
        if get_faulty_level_index(report) is None:
            safe_reports += 1
    print(safe_reports)


def task2(cnt):
    safe_reports = 0
    reports = parse_cnt(cnt)
    for report in reports:
        if (idx := get_faulty_level_index(report)) is None:
            safe_reports += 1
            continue
        for offset in [0, -1, -2]:
            if idx + offset < 0:
                continue
            if get_faulty_level_index(report[:idx + offset] + report[idx + offset + 1:]) is None:
                safe_reports += 1
                break
    print(safe_reports)
