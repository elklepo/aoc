import heapq


def dijkstra_with_path(graph, start_vertex, end_vertex):
    d, previous = {v: float('inf') for v in graph}, {v: None for v in graph}
    d[start_vertex] = 0
    pq = [(0, start_vertex)]
    while pq:
        dist, u = heapq.heappop(pq)
        if u == end_vertex:
            path = []
            while u:
                path.append(u)
                u = previous[u]
            return path[::-1]
        for v in graph[u]:
            if (new_dist := d[u] + 1) < d[v]:
                d[v], previous[v] = new_dist, u
                heapq.heappush(pq, (new_dist, v))
    return None


def parse_cnt(cnt):
    graph = {(x, y): set() for x in range(71) for y in range(71)}
    for x, y in graph:
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if (x + dx, y + dy) in graph:
                graph[(x, y)].add((x + dx, y + dy))

    bits = [tuple(map(int, l.split(','))) for l in cnt.splitlines()]
    return graph, bits


def task1(cnt):
    graph, bits = parse_cnt(cnt)
    for b in bits[:1024]:
        for n in graph.pop(b, set()):
            graph[n].discard(b)
    print(len(dijkstra_with_path(graph, (0, 0), (70, 70))) - 1)


def task2(cnt):
    graph, bits = parse_cnt(cnt)
    path = None
    for i, b in enumerate(bits):
        for n in graph.pop(b, set()):
            graph[n].discard(b)
        if i >= 1024 and (not path or b in path):
            path = dijkstra_with_path(graph, (0, 0), (70, 70))
            if path is None:
                print(f'{b[0]},{b[1]}')
                break