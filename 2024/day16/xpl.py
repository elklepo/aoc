import heapq
from collections import defaultdict


def dijkstra_all_paths(graph, start, end_nodes):
    all_shortest_paths = []
    min_cost = float('inf')
    pq = [(0, s:=0, start, [start])]
    path_costs = defaultdict(lambda: float('inf')) | {start: 0}

    while pq:
        cost, _, current_node, path = heapq.heappop(pq)
        if cost > min_cost:
            break

        if current_node in end_nodes:
            if cost < min_cost:
                min_cost = cost
                all_shortest_paths = [path]
            elif cost == min_cost:
                all_shortest_paths.append(path)
            continue

        for neighbor, edge_cost in graph[current_node].items():
            new_cost = cost + edge_cost
            if new_cost <= path_costs[neighbor]:
                path_costs[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, s:=s+1, neighbor, path + [neighbor]))

    return all_shortest_paths, min_cost


def parse_cnt(cnt):
    grid = {
        (y + x * 1j): c
        for y, l in enumerate(cnt.splitlines())
        for x, c in enumerate(l)
    }
    graph = defaultdict(dict)
    for n in grid:
        if grid[n] != '#':
            graph[(n, True)][(n, False)] = 1000
            graph[(n, False)][(n, True)] = 1000
            for d in [-1, 1j, 1, -1j]:
                if grid[n + d] != '#':
                    graph[(n, bool(d.imag))][(n + d, bool(d.imag))] = 1

    return graph, next(m for m in grid if grid[m] == 'S'), next(m for m in grid if grid[m] == 'E')


def task1(cnt):
    graph, start, end = parse_cnt(cnt)
    shortest_path = dijkstra_all_paths(graph,(start, True), [(end, True), (end, False)])
    print(shortest_path[1])


def task2(cnt):
    graph, start, end = parse_cnt(cnt)
    shortest_path = dijkstra_all_paths(graph,(start, True), [(end, True), (end, False)])
    print(len({e[0] for path in shortest_path[0] for e in path}))