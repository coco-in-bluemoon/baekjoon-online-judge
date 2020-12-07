'''Note
가장 일찍 끝나는 것 순서대로 모으면 최대 회의의 개수를 구할 수 있다.
'''


import heapq


def solution(timelines):
    heap = list()

    for start, end in timelines:
        heapq.heappush(heap, (end, start))

    counter = 0
    time = -1
    while heap:
        end, start = heapq.heappop(heap)
        if start < time:
            continue
        counter += 1
        time = end

    return counter


if __name__ == "__main__":
    num_timeline = int(input())
    timelines = list()
    for _ in range(num_timeline):
        start, end = map(int, input().split())
        timelines.append((start, end))
    answer = solution(timelines)
    print(answer)
