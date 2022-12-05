import importlib
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(f'usage: python3 {sys.argv[0]} <day_number>')

    day = sys.argv[1]

    day_module = importlib.import_module(f'day{day}.xpl')

    with open(f'./day{day}/input0', 'r') as f:
        cnt0 = f.read().rstrip()

    with open(f'./day{day}/input1', 'r') as f:
        cnt1 = f.read().rstrip()

    if hasattr(day_module, 'task1'):
        print("### TASK 1 - INPUT 0 ###")
        day_module.task1(cnt0)
        print("### TASK 1 - INPUT 1 ###")
        day_module.task1(cnt1)

    if hasattr(day_module, 'task2'):
        print("### TASK 2 - INPUT 0 ###")
        day_module.task2(cnt0)
        print("### TASK 2 - INPUT 1 ###")
        day_module.task2(cnt1)
