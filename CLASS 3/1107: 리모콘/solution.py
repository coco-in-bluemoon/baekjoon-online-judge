def is_dialable(number, broken):
    for n in str(number):
        if n in broken:
            return False
    return True


def solution(target, broken):
    START = 100
    broken = set(str(broken))

    difference = abs(target - START)
    answer = difference

    for delta in range(difference):
        target_bigger = target + delta
        target_smaller = target - delta

        if target_smaller >= 0 and is_dialable(target_smaller, broken):
            counter = len(str(target_smaller)) + delta
            answer = min(answer, counter)
            break
        elif is_dialable(target_bigger, broken):
            counter = len(str(target_bigger)) + delta
            answer = min(answer, counter)
            break

    return answer


if __name__ == "__main__":
    assert solution(5457, [6, 7, 8]) == 6
    assert solution(100, [0, 1, 2, 3, 4]) == 0
    assert solution(500000, [0, 2, 3, 4, 6, 7, 8, 9]) == 11117
    assert solution(0, [0, 1, 2]) == 4

    target = int(input())
    n = int(input())
    broken = list()
    if n:
        broken = list(map(int, input().split()))
    answer = solution(target, broken)
    print(answer)
