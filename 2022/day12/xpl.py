from queue import PriorityQueue
from collections import defaultdict


def _dijkstra(graph, start_vertex):
    vertices = graph.keys()
    d = {v: float('inf') for v in vertices}
    d[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, u) = pq.get()

        for v in graph[u]:
            if d[v] > d[u] + 1:
                d[v] = d[u] + 1
                pq.put((d[v], v))
    return d


def _init_reverse_graph(grid):
    # we'll be looking for paths from the destination, not the start
    # so the graph needs to be built according to reverse task rules
    graph = defaultdict(list)
    for y, row in enumerate(grid):
        for x, elem in enumerate(row):
            if y > 0 and grid[y-1][x] <= grid[y][x] + 1:
                graph[(y-1, x)].append((y, x))
            if y < len(grid) - 1 and grid[y+1][x] <= grid[y][x] + 1:
                graph[(y+1, x)].append((y, x))
            if x > 0 and grid[y][x-1] <= grid[y][x] + 1:
                graph[(y, x-1)].append((y, x))
            if x < len(grid[0]) - 1 and grid[y][x+1] <= grid[y][x] + 1:
                graph[(y, x+1)].append((y, x))
    return graph


def _parse_grid(lines):
    grid = [list(l) for l in lines]
    sy, sx = [(y, x) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == 'S'][0]
    ey, ex = [(y, x) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == 'E'][0]
    grid[sy][sx] = 'a'
    grid[ey][ex] = 'z'
    grid = [[ord(c) - ord('a') for c in row] for row in grid]
    return grid, (sy, sx), (ey, ex)


def task1(cnt):
    grid, start, end = _parse_grid(cnt.splitlines())

    graph = _init_reverse_graph(grid)

    d = _dijkstra(graph, end)
    print(d[start])


def task2(cnt):
    grid, start, end = _parse_grid(cnt.splitlines())

    graph = _init_reverse_graph(grid)

    d = _dijkstra(graph, end)

    all_lowest_points = [(y, x) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == 0]
    print(min(d[point] for point in all_lowest_points))
