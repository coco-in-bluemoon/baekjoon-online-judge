def factorize_by(number, by):
    counter = 0
    while not number % by:
        counter += 1
        number //= by

    return counter


def count_two_five_in_factorial(number, cache):
    if number in cache:
        return

    num_two = factorize_by(number, 2)
    num_five = factorize_by(number, 5)

    count_two_five_in_factorial(number-1, cache)

    total_num_two = num_two + cache[number-1][0]
    total_num_five = num_five + cache[number-1][1]

    cache[number] = (total_num_two, total_num_five)


def solution(number):
    cache = {0: (0, 0), 1: (0, 0)}
    count_two_five_in_factorial(number, cache)
    counter_two, counter_five = cache[number]

    return min(counter_two, counter_five)


if __name__ == "__main__":
    number = int(input())
    answer = solution(number)
    print(answer)
