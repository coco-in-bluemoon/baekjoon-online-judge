def count_zero_and_one(n, cache):
    if n in cache:
        return cache[n]

    minus_one = count_zero_and_one(n-1, cache)
    minus_two = count_zero_and_one(n-2, cache)

    cache[n] = [minus_one[0] + minus_two[0], minus_one[1] + minus_two[1]]
    return cache[n]


def solution(n):
    cache = {0: [1, 0], 1: [0, 1]}
    answer = count_zero_and_one(n, cache)
    return answer


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        answer = solution(n)
        print('{} {}'.format(answer[0], answer[1]))
