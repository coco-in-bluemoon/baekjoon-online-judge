from collections import deque


def solution(start, target):
    counter = 0
    visited = set()
    queue = deque([(start, counter)])
    while queue:
        position, counter = queue.popleft()
        if position in visited:
            continue
        visited.add(position)

        if position == target:
            break

        if (position > 0) and (position - 1 not in visited):
            queue.append((position - 1, counter + 1))

        if (position < 2 * target) and (position + 1 not in visited):
            queue.append((position + 1, counter + 1))

        if (position < 2 * target) and (position * 2 not in visited):
            queue.append((position * 2, counter + 1))

    return counter


if __name__ == "__main__":
    assert solution(5, 17) == 4

    start, target = map(int, input().split())
    answer = solution(start, target)
    print(answer)
