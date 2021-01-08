from collections import deque


def solution(target):
    queue = deque([('', 0)])
    counter = 0
    visited = set()
    while queue:
        expression, value = queue.popleft()
        if value == target:
            counter += 1

        for num in range(1, 4):
            next_expression = expression + str(num)
            next_value = value + num

            if next_expression in visited or next_value > target:
                continue

            queue.append((next_expression, next_value))

    return counter


if __name__ == "__main__":
    num_test = int(input())
    for _ in range(num_test):
        target = int(input())
        answer = solution(target)
        print(answer)
