from typing import cast


def solution(target, base):
    target_in_base = [False] * len(target)
    for idx, number in enumerate(target):
        try:
            base.index(number) >= 0
            target_in_base[idx] = True
        except ValueError:
            continue
    return target_in_base


if __name__ == "__main__":
    N = int(input())
    base = list(map(int, input().split()))
    M = int(input())
    target = list(map(int, input().split()))

    answer = solution(target, base)
    print('\n'.join(['1' if boolean else '0' for boolean in answer]))
