from collections import deque


def solution(num_node, edges):
    START_NODE = 1
    graph = {node: set() for node in range(1, num_node+1)}

    for src, dst in edges:
        graph[src].add(dst)
        graph[dst].add(src)

    visited = {node: False for node in range(1, num_node+1)}
    queue = deque([START_NODE])
    counter = 0
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True

        if node != START_NODE:
            counter += 1

        for adjacent_node in graph[node]:
            if visited[adjacent_node]:
                continue
            queue.append(adjacent_node)

    return counter


if __name__ == "__main__":
    num_node = int(input())
    num_edge = int(input())
    edges = list()
    for _ in range(num_edge):
        src, dst = map(int, input().split())
        edges.append([src, dst])
    answer = solution(num_node, edges)
    print(answer)
