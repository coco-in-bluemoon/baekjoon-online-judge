from collections import deque
import re


def solution(commands, numbers):
    REVERSE = 'R'
    DELETE = 'D'

    commands = re.sub('RR', '', commands)
    array_reversed = False
    queue = deque(numbers)

    for command in commands:
        if command == REVERSE:
            array_reversed = False if array_reversed else True
        elif command == DELETE:
            if not queue:
                return None
            if array_reversed:
                queue.pop()
            else:
                queue.popleft()

    results = list(queue)[::-1] if array_reversed else list(queue)
    return results


if __name__ == "__main__":
    num_test = int(input())
    for _ in range(num_test):
        commands = input().strip()
        num_number = int(input())
        numbers = re.findall('[0-9]+', input())
        answer = solution(commands, numbers)
        if answer is None:
            print('error')
        else:        
            answer_with_print_format = '[' + ','.join([str(number) for number in answer]) + ']'
            print(answer_with_print_format)
