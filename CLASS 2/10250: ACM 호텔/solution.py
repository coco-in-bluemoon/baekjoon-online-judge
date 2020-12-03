import math


def solution(height, width, target):
    no = math.ceil(target / height)
    floor = target % height
    floor = height if not floor else floor

    return '{:d}{:02}'.format(floor, no)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        height, width, target = map(int, input().split())
        answer = solution(height, width, target)
        print(answer)
