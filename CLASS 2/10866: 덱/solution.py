from collections import deque


def solution(commands):
    dq = deque([])
    log = list()
    for command in commands:
        command = command.split()
        if len(command) == 2:
            command, number = command
            if command == 'push_front':
                dq.appendleft(number)
            elif command == 'push_back':
                dq.append(number)
        else:
            command = command[0]

            if command == 'pop_front':
                if not dq:
                    log.append(-1)
                else:
                    log.append(dq.popleft())
            elif command == 'pop_back':
                if not dq:
                    log.append(-1)
                else:
                    log.append(dq.pop())
            elif command == 'size':
                log.append(len(dq))
            elif command == 'empty':
                log.append(0 if dq else 1)
            elif command == 'front':
                if not dq:
                    log.append(-1)
                else:
                    log.append(dq[0])
            elif command == 'back':
                if not dq:
                    log.append(-1)
                else:
                    log.append(dq[-1])

    return log


if __name__ == "__main__":
    n = int(input())
    commands = list()
    for _ in range(n):
        commands.append(input().strip())
    answer = solution(commands)
    print('\n'.join([str(log) for log in answer]))
