from collections import defaultdict


def parse_cnt(cnt):
    grid, moves = cnt.split('\n\n')
    grid = defaultdict(str) | {
        (y + x * 1j): c
        for y, l in enumerate(grid.splitlines())
        for x, c in enumerate(l)
    }
    moves = [{'^': -1, '>': 1j, 'v': 1, '<': -1j}[m] for m in moves.replace('\n', '')]
    return grid, moves


def simulate(grid, moves):
    pos = next(k for k, v in grid.items() if v == '@')
    for m in moves:
        to_move = []
        q = [pos]
        while q:
            p = q.pop()
            if grid[p] in ['#', '']:
                break
            elif grid[p] != '.':
                to_move.append(p)
                np = p + m
                q.append(np)
                if not m.imag and grid[np] == '[':
                    q.append(np + 1j)
                if not m.imag and grid[np] == ']':
                    q.append(np - 1j)
        else:
            seen = set()
            for p in reversed(to_move):
                if p not in seen:
                    seen.add(p)
                    grid[p], grid[p + m] = grid[p + m], grid[p]
            pos += m


def task1(cnt):
    grid, moves = parse_cnt(cnt)
    simulate(grid, moves)
    print(sum(n.real * 100 + n.imag for n in grid if grid[n] == 'O'))


def task2(cnt):
    grid, moves = parse_cnt(cnt.replace('O', '[]').replace('.', '..').replace('#', '##').replace('@', '@.'))
    simulate(grid, moves)
    print(sum(n.real * 100 + n.imag for n in grid if grid[n] == '['))