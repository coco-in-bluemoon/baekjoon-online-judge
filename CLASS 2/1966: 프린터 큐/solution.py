from collections import deque


def solution(document, priority):
    queue = deque([(score, index) for index, score in enumerate(priority)])
    max_priority = max(queue)[0]

    counter_turn = 1
    while queue:
        score, index = queue.popleft()
        if score < max_priority:
            queue.append((score, index))
        else:
            if index == document:
                break
            max_priority = max(queue)[0]
            counter_turn += 1

    return counter_turn


if __name__ == "__main__":
    assert solution(2, [1, 2, 3, 4]) == 2

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        priority = list(map(int, input().split()))

        answer = solution(M, priority)
        print(answer)
