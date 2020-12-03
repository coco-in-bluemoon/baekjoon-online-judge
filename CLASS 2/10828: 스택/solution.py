from collections import deque


def solution(commands):
    stack = deque([])
    log = list()
    for command in commands:
        command = command.split()
        if len(command) == 2:
            command, number = command
            stack.append(number)
        else:
            command = command[0]

            if command == 'pop':
                if not stack:
                    log.append(-1)
                else:
                    log.append(stack.pop())
            elif command == 'size':
                log.append(len(stack))
            elif command == 'empty':
                log.append(0 if stack else 1)
            elif command == 'top':
                if not stack:
                    log.append(-1)
                else:
                    log.append(stack[-1])

    return log


if __name__ == "__main__":
    n = int(input())
    commands = list()
    for _ in range(n):
        commands.append(input().strip())
    answer = solution(commands)
    print('\n'.join([str(log) for log in answer]))
