import importlib
import sys
import time


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit(f'usage: python3 {sys.argv[0]} <year> <day>')

    year, day = sys.argv[1], sys.argv[2]
    day_dir_name = f'day{day.rjust(2, "0")}'

    day_module = importlib.import_module(f'{year}.{day_dir_name}.xpl')

    with open(f'{year}/{day_dir_name}/input0', 'r') as f:
        cnt0 = f.read().rstrip()

    with open(f'{year}/{day_dir_name}/input1', 'r') as f:
        cnt1 = f.read().rstrip()

    def _measure_time(foo):
        start = time.time()
        foo()
        print(f'took {time.time() - start:.2f}s')

    if hasattr(day_module, 'task1'):
        print(f'### {year} DAY {day} - TASK 1 - TEST INPUT ###')
        _measure_time(lambda: day_module.task1(cnt0))

        print(f'### {year} DAY {day} - TASK 1 - CHALLENGE INPUT ###')
        _measure_time(lambda: day_module.task1(cnt1))

    if hasattr(day_module, 'task2'):
        print(f'### {year} DAY {day} - TASK 2 - TEST INPUT ###')
        _measure_time(lambda: day_module.task2(cnt0))

        print(f'### {year} DAY {day} - TASK 2 - CHALLENGE INPUT ###')
        _measure_time(lambda: day_module.task2(cnt1))
