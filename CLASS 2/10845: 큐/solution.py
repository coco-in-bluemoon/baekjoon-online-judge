from collections import deque


def solution(commands):
    queue = deque([])
    log = list()
    for command in commands:
        command = command.split()
        if len(command) == 2:
            command, number = command
            queue.append(number)
        else:
            command = command[0]

            if command == 'pop':
                if not queue:
                    log.append(-1)
                else:
                    log.append(queue.popleft())
            elif command == 'size':
                log.append(len(queue))
            elif command == 'empty':
                log.append(0 if queue else 1)
            elif command == 'front':
                if not queue:
                    log.append(-1)
                else:
                    log.append(queue[0])
            elif command == 'back':
                if not queue:
                    log.append(-1)
                else:
                    log.append(queue[-1])

    return log


if __name__ == "__main__":
    n = int(input())
    commands = list()
    for _ in range(n):
        commands.append(input().strip())
    answer = solution(commands)
    print('\n'.join([str(log) for log in answer]))
