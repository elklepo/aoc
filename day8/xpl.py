from enum import Enum


class Direction(Enum):
    LEFT = 1,
    TOP = 2,
    RIGHT = 3,
    DOWN = 4


class Tree:
    def __init__(self, height):
        self.h = height
        self.neigh = {direction: None for direction in Direction}

    def get_block(self, d: Direction):
        ptr = self.neigh[d]
        distance = 0
        while ptr is not None:
            distance += 1
            if ptr.h >= self.h:
                break
            ptr = ptr.neigh[d]
        return ptr, distance

    def is_visible(self):
        return self.get_block(Direction.LEFT)[0] is None or \
               self.get_block(Direction.TOP)[0] is None or \
               self.get_block(Direction.RIGHT)[0] is None or \
               self.get_block(Direction.DOWN)[0] is None

    def get_score(self):
        return self.get_block(Direction.LEFT)[1] * \
               self.get_block(Direction.TOP)[1] * \
               self.get_block(Direction.RIGHT)[1] * \
               self.get_block(Direction.DOWN)[1]


def _parse_grid(raw_grid):
    dim = len(raw_grid)
    grid = [[Tree(int(raw_grid[y][x])) for x in range(dim)] for y in range(dim)]
    for y in range(dim):
        for x in range(dim):
            grid[y][x].neigh[Direction.LEFT] = grid[y][x - 1] if x > 0 else None
            grid[y][x].neigh[Direction.TOP] = grid[y - 1][x] if y > 0 else None
            grid[y][x].neigh[Direction.RIGHT] = grid[y][x + 1] if x < dim - 1 else None
            grid[y][x].neigh[Direction.DOWN] = grid[y + 1][x] if y < dim - 1 else None
    return grid


def task1(cnt):
    grid = _parse_grid(cnt.splitlines())
    dim = len(grid)
    print(sum(sum(grid[y][x].is_visible() for y in range(dim)) for x in range(dim)))


def task2(cnt):
    grid = _parse_grid(cnt.splitlines())
    dim = len(grid)
    print(max(max(grid[y][x].get_score() for y in range(dim)) for x in range(dim)))