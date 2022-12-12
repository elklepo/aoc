def emulate(instructions, hook):
    cycles_count = 0
    reg = 1
    instructions = [(i, 2) if i.startswith('addx') else (i, 1) for i in instructions][::-1]
    while instructions:
        cycles_count += 1
        hook(cycles_count, reg)

        ins, cycles = instructions.pop()
        cycles -= 1
        if cycles == 0:
            if ins.startswith('addx'):
                reg += int(ins.split(' ')[1])
            else:
                pass
        else:
            instructions.append((ins, cycles,))


def task1(cnt):
    probes = [20, 60, 100, 140, 180, 220]
    results = []

    def hook(cycles_count, reg):
        if cycles_count in probes:
            results.append((cycles_count, reg))

    emulate(cnt.splitlines(), hook)
    print(sum(r[0] * r[1] for r in results))


def task2(cnt):
    def hook(cycles_count, reg):
        position = (cycles_count - 1) % 40
        if reg - 1 <= position <= reg + 1:
            print('X', end='')
        else:
            print('.', end='')
        if position == 39:
            print('')

    emulate(cnt.splitlines(), hook)
