from collections import defaultdict
import heapq


def delete_value(heap, deleted):
    while heap:
        _, index = heapq.heappop(heap)
        if not deleted[index]:
            deleted[index] = True
            break

def solution(commands):
    min_heap = list()
    max_heap = list()

    deleted = defaultdict(lambda: False)

    index = 0
    for operation, value in commands:
        if operation == 'I':
            value = int(value)
            heapq.heappush(max_heap, (-value, index))
            heapq.heappush(min_heap, (value, index))
            index += 1
        elif operation == 'D':
            if value == '1':
                delete_value(max_heap, deleted)
            elif value == '-1':
                delete_value(min_heap, deleted)

    min_value, max_value = None, None

    while min_heap and min_value is None:
        value, index = heapq.heappop(min_heap)
        if not deleted[index]:
            min_value = value
    while max_heap and max_value is None:
        value, index = heapq.heappop(max_heap)
        if not deleted[index]:
            max_value = -value

    if min_value is None or max_value is None:
        return 'EMPTY'
    else:
        return '{} {}'.format(max_value, min_value)


if __name__ == "__main__":
    num_test = int(input())
    for _ in range(num_test):
        num_command = int(input())
        commands = list()
        for _ in range(num_command):
            commands.append(input().split())
        answer = solution(commands)
        print(answer)
