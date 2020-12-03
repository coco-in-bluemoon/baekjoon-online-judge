def solution(numbers):
    return list(sorted(numbers))


if __name__ == "__main__":
    n = int(input())
    numbers = list()
    for _ in range(n):
        numbers.append(int(input()))
    answer = solution(numbers)

    print('\n'.join(str(number) for number in answer))
