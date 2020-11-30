def solution(num_a, num_b):
    return [
        num_a + num_b, num_a - num_b, num_a * num_b,
        num_a // num_b, num_a % num_b
    ]


if __name__ == "__main__":
    assert solution(7, 3) == [10, 4, 21, 2, 1]

    num_a, num_b = map(int, input().split())
    answer = solution(num_a, num_b)
    print('\n'.join([str(num) for num in answer]))
