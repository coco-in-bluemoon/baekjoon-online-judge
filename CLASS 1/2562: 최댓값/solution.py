import math


def solution(numbers):
    max_number = -math.inf
    max_number_index = -1

    for idx, number in enumerate(numbers):
        if number > max_number:
            max_number = number
            max_number_index = idx + 1

    return [max_number, max_number_index]


if __name__ == "__main__":
    numbers = [3, 29, 38, 12, 57, 74, 40, 85, 61]
    assert solution(numbers) == [85, 8]

    numbers = list()
    for _ in range(9):
        number = int(input())
        numbers.append(number)

    answer = solution(numbers)
    print('%d %d' % (answer[0], answer[1]))
