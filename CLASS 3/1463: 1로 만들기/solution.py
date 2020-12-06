'''Note
3으로 나누어 떨어지면서 2로 나누어 떨어지는 수도 있습니다.
'''
from collections import deque


def solution(target):
    counter = 0
    visited = set()
    queue = deque([(target, counter)])

    while queue:
        number, counter = queue.popleft()

        if number in visited:
            continue

        if number == 1:
            break

        if not number % 3:
            next_number = number // 3
            if next_number not in visited:
                queue.append((next_number, counter + 1))

        if not number % 2:
            next_number = number // 2
            if next_number not in visited:
                queue.append((next_number, counter + 1))

        next_number = number - 1
        if next_number not in visited:
            queue.append((next_number, counter + 1))

    return counter


if __name__ == "__main__":
    target = int(input())
    answer = solution(target)
    print(answer)
