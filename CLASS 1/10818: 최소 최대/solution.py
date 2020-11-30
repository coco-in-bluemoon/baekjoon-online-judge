def solution(numbers):
    return [min(numbers), max(numbers)]


if __name__ == "__main__":
    numbers = [20, 10, 35, 30, 7]
    assert solution(numbers) == [7, 35]

    n = int(input())
    numbers = list(map(int, input().split()))
    answer = solution(numbers)
    print('{} {}'.format(answer[0], answer[1]))
