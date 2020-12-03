from itertools import combinations


def solution(target, numbers):
    answer = 0
    for triplets in combinations(numbers, 3):
        triple_sum = sum(triplets)
        if triple_sum > target:
            continue
        answer = max(answer, sum(triplets))

    return answer


if __name__ == "__main__":
    n, target = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = solution(target, numbers)
    print(answer)
