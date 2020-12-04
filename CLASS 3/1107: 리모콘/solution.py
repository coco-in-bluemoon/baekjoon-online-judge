def solution(target, broken):
    START = 100
    broken = set(broken)

    if target == START:
        return 0

    target_bigger = target
    target_set = set(map(int, str(target_bigger)))
    while len(broken & target_set):
        target_bigger += 1
        target_set = set(map(int, str(target_bigger)))
    counter_bigger = len(str(target_bigger)) + abs(target_bigger - target)

    target_smaller = target
    target_set = set(map(int, str(target_smaller)))
    while len(broken & target_set):
        target_smaller -= 1
        target_set = set(map(int, str(target_smaller)))
    counter_smaller = len(str(target_smaller)) + abs(target - target_smaller)

    return min(counter_smaller, counter_bigger)


if __name__ == "__main__":
    assert solution(5457, [6, 7, 8]) == 6
    assert solution(100, [0, 1, 2, 3, 4]) == 0
    assert solution(500000, [0, 2, 3, 4, 6, 7, 8, 9]) == 11117

    target = int(input())
    n = int(input())
    broken = list(map(int, input().split()))
    answer = solution(target, broken)
    print(answer)
