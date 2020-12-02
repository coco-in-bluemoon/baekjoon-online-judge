def solution(target):
    distance = 1
    source = 1
    while source < target:
        source += (6 * distance)
        distance += 1

    return distance


if __name__ == "__main__":
    target = int(input())
    answer = solution(target)
    print(answer)
