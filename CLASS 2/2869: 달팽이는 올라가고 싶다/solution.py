import math


def solution(up, down, height):
    counter_day = 1

    if up < height:
        counter_day += math.ceil((height - up) / (up - down))

    return counter_day


if __name__ == "__main__":
    up, down, height = map(int, input().split())
    answer = solution(up, down, height)
    print(answer)
