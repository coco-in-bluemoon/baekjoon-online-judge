def solution(numbers):
    numbers_reversed = [int(str(number)[::-1]) for number in numbers]
    return max(numbers_reversed)


if __name__ == "__main__":
    numbers = [734, 893]
    assert solution(numbers) == 437

    numbers = list(map(int, input().split()))
    answer = solution(numbers)
    print(answer)
