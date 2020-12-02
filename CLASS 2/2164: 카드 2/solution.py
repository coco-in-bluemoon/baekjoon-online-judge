from collections import deque


def solution(n):
    queue = deque(range(1, n+1))
    while len(queue) > 1:
        queue.popleft()
        top = queue.popleft()
        queue.append(top)
    return queue[0]


if __name__ == "__main__":
    n = int(input())
    answer = solution(n)
    print(answer)
