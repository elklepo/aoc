import re
from functools import cache
from queue import PriorityQueue


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


def _parse_lines(lines):
    pat = r'Valve ([A-Z]+) has flow rate=([0-9]+);[a-z ]+([A-Z, ]+)'.strip()
    valves = {}
    graph = {}
    for valve, flow, neighs in (re.search(pat, m).groups() for m in lines):
        valves[valve] = int(flow)
        graph[valve] = [neigh.strip() for neigh in neighs.split(',')]

    return valves, {k: _dijkstra(graph, k) for k in graph.keys()}


def _solve(cnt, elephant_mode):
    valves, move_costs = _parse_lines(cnt.splitlines())

    @cache
    def _get_best(curr: str, time: int, valves_to_open: frozenset, parallel: bool):
        # Check what gives more profit:

        # 1) covering remaining `valves_to_open` by "elephant" from start point
        total = 0 if not parallel else _get_best("AA", 26, valves_to_open, False)

        # 2) covering one more element from `valves_to_open` by "me" and the rest by "me" or "elephant"
        for candidate in valves_to_open:
            new_time = time - move_costs[curr][candidate] - 1
            if new_time >= 0:
                candidate_total = _get_best(candidate, new_time, valves_to_open - {candidate}, parallel)
                total = max(total, new_time * valves[candidate] + candidate_total)
        return total

    return _get_best('AA', 26 if elephant_mode else 30, frozenset(x for x in valves if valves[x] > 0), elephant_mode)


def task1(cnt):
    print(_solve(cnt, elephant_mode=False))


def task2(cnt):
    print(_solve(cnt, elephant_mode=True))
