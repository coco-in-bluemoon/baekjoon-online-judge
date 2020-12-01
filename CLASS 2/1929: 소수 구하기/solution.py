def is_prime_number(number):
    if number <= 1:
        return False

    for divider in range(2, int(number ** 0.5) + 1):
        if not (number % divider):
            return False
    return True


def solution(start, end):
    prime_numbers = list()
    for number in range(start, end+1):
        if is_prime_number(number):
            prime_numbers.append(number)

    return prime_numbers


if __name__ == "__main__":
    start, end = map(int, input().split())
    answer = solution(start, end)
    print('\n'.join([str(number) for number in answer]))
