def solution(numbers, x):
    return [number for number in numbers if number < x]


if __name__ == "__main__":
    n, x = 10, 5
    numbers = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]
    assert solution(numbers, x) == [1, 4, 2, 3]

    n, x = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = solution(numbers, x)
    print(' '.join(str(num) for num in answer))
