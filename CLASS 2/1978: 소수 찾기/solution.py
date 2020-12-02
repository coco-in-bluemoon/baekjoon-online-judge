def is_prime_number(number):
    if number < 2:
        return False

    for divider in range(2, int(number ** 0.5) + 1):
        if not number % divider:
            return False
    return True


def solution(numbers):
    counter = 0
    for number in numbers:
        counter += int(is_prime_number(number))

    return counter


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    answer = solution(numbers)
    print(answer)
