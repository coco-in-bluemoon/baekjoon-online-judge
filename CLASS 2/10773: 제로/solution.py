from collections import deque


def solution(commands):
    ZERO = 0
    stack = deque([])
    for command in commands:
        if command == ZERO:
            stack.pop()
        else:
            stack.append(command)

    return sum(stack)


if __name__ == "__main__":
    n = int(input())
    commands = list()
    for _ in range(n):
        commands.append(int(input()))
    answer = solution(commands)
    print(answer)
