from collections import defaultdict
from collections import deque


def dfs(graph, start_node):
    order = list()
    visited = set()
    stack = deque([start_node])

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        for adjacent_node in graph[node][::-1]:
            if adjacent_node in visited:
                continue
            stack.append(adjacent_node)

    return order


def bfs(graph, start_node):
    order = list()
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        for adjacent_node in graph[node]:
            if adjacent_node in visited:
                continue
            queue.append(adjacent_node)

    return order


def solution(edges, start_node):
    graph = defaultdict(list)
    for src, dst in edges:
        graph[src].append(dst)
        graph[dst].append(src)

    for node in graph.keys():
        graph[node] = sorted(graph[node])

    dfs_order = dfs(graph, start_node)
    bfs_order = bfs(graph, start_node)

    return dfs_order, bfs_order


if __name__ == "__main__":
    num_node, num_edge, start_node = map(int, input().split())
    edges = list()
    for _ in range(num_edge):
        src, dst = map(int, input().split())
        edges.append([src, dst])
    dfs_order, bfs_order = solution(edges, start_node)
    print(' '.join([str(node) for node in dfs_order]))
    print(' '.join([str(node) for node in bfs_order]))
