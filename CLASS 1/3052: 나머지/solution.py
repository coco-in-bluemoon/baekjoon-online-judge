def solution(numbers):
    DIVIDER = 42

    remainders = set()
    for number in numbers:
        remainder = number % 42
        remainders.add(remainder)

    return len(remainders)


if __name__ == "__main__":
    numbers = [39, 40, 41, 42, 43, 44, 82, 83, 84, 85]
    assert solution(numbers) == 6

    NUM_CASE = 10
    numbers = list()
    for _ in range(NUM_CASE):
        number = int(input())
        numbers.append(number)
    answer = solution(numbers)
    print(answer)
