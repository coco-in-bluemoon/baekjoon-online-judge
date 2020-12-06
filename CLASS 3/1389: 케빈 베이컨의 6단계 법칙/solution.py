from collections import deque
import math


def calculate_kevin_bacon_score(target, graph):
    distances = {friend: math.inf for friend in graph.keys()}
    distances[target] = 0
    queue = deque([target])

    while queue:
        node = queue.popleft()

        for friend in graph[node]:
            if distances[friend] < distances[node] + 1:
                continue

            distances[friend] = distances[node] + 1
            queue.append(friend)

    return sum(distances.values())


def solution(num_friend, friends):
    graph = {friend: set() for friend in range(1, num_friend+1)}
    for src, dst in friends:
        graph[src].add(dst)
        graph[dst].add(src)

    kevin_bacon_scores = {friend: 0 for friend in range(1, num_friend+1)}
    for target in range(1, num_friend+1):
        score = calculate_kevin_bacon_score(target, graph)
        kevin_bacon_scores[target] = score

    kevin_bacon_scores = sorted(kevin_bacon_scores.items(), key=lambda x: (x[1], x[0]))
    return kevin_bacon_scores[0][0]


if __name__ == "__main__":
    num_node, num_edge = map(int, input().split())
    friends = list()
    for _ in range(num_edge):
        src, dst = map(int, input().split())
        friends.append([src, dst])

    answer = solution(num_node, friends)
    print(answer)
