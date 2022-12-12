def _parse_init_state(lines) -> dict[int, list]:
    items, stacks_cnt = lines[:-1], int(lines[-1].rstrip()[-1])

    state = {i + 1: [] for i in range(stacks_cnt)}
    for layer in items[::-1]:
        # starting from index 1 the items are every 4th character
        items = (layer[i] for i in range(1, len(layer), 4))
        for i, item in enumerate(items):
            if item != ' ':
                state[i + 1].append(item)
    return state


def _parse_instructions(lines) -> list[tuple[int]]:
    return [tuple(int(s) for s in line.split() if s.isdigit()) for line in lines]


def task1(cnt):
    raw_state, raw_instructions = cnt.split('\n\n')
    state = _parse_init_state(raw_state.splitlines())
    instructions = _parse_instructions(raw_instructions.splitlines())

    for num, src, dst in instructions:
        for _ in range(num):
            state[dst].append(state[src].pop())

    print(''.join(s.pop() for s in state.values()))


def task2(cnt):
    raw_state, raw_instructions = cnt.split('\n\n')
    state = _parse_init_state(raw_state.splitlines())
    instructions = _parse_instructions(raw_instructions.splitlines())

    for num, src, dst in instructions:
        items = [state[src].pop() for _ in range(num)][::-1]
        for item in items:
            state[dst].append(item)

    print(''.join(s.pop() for s in state.values()))
