class Knot:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def move(self, y, x):
        self.y += y
        self.x += x

    def move_to(self, front):
        if (self.y - 1 <= front.y <= self.y + 1) and (self.x - 1 <= front.x <= self.x + 1):
            return  # knots already next to each other
        y_dist, x_dist = front.y - self.y, front.x - self.x
        my = 0 if y_dist == 0 else y_dist // abs(y_dist)
        mx = 0 if x_dist == 0 else x_dist // abs(x_dist)
        self.move(y=my, x=mx)


def _get_visited_by_tail(rope, moves):
    directions = {
        'L': (0, -1),
        'U': (1, 0),
        'R': (0, 1),
        'D': (-1, 0),
    }
    head, tail = rope[0], rope[-1]
    visited = set()
    visited.add((tail.y, tail.x))
    for move in moves:
        direction, steps = move.split(' ')
        dy, dx = directions[direction]
        for _ in range(int(steps)):
            rope[0].move(y=dy, x=dx)
            for i in range(1, len(rope)):
                rope[i].move_to(rope[i-1])
            visited.add((tail.y, tail.x))
    return visited


def task1(cnt):
    moves = cnt.splitlines()
    rope = [Knot(0, 0) for _ in range(2)]
    print(len(_get_visited_by_tail(rope, moves)))


def task2(cnt):
    moves = cnt.splitlines()
    rope = [Knot(0, 0) for _ in range(10)]
    print(len(_get_visited_by_tail(rope, moves)))