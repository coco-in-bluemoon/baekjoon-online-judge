import heapq


def solution(commands):
    heap = list()
    results = list()
    for command in commands:
        if command:
            heapq.heappush(heap, command)
        else:
            result = 0
            if heap:
                result = heapq.heappop(heap)
            results.append(result)

    return results


if __name__ == "__main__":
    n = int(input())
    commands = list()
    for _ in range(n):
        commands.append(int(input()))

    answer = solution(commands)
    print('\n'.join([str(number) for number in answer]))
