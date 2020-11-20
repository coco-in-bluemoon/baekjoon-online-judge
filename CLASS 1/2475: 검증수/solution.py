def solution(numbers):
    squared_sum = sum([number ** 2 for number in numbers])
    validation_number = squared_sum % 10
    return validation_number


if __name__ == "__main__":
    numbers = [0, 4, 2, 5, 6]
    assert solution(numbers) == 1

    numbers = list(map(int, input().split()))
    answer = solution(numbers)
    print(answer)
