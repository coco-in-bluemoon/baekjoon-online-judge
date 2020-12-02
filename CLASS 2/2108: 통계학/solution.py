from collections import defaultdict


def solution(numbers):
    numbers = list(sorted(numbers))
    mean = round(sum(numbers) / len(numbers))
    median = numbers[len(numbers) // 2]

    number_freq = defaultdict(int)
    for number in numbers:
        number_freq[number] += 1

    number_freq = sorted(number_freq.items(), key=lambda x: (-x[1], x[0]))
    most_frequent = number_freq[0][0]
    if len(number_freq) >= 2 and number_freq[0][1] == number_freq[1][1]:
        most_frequent = number_freq[1][0]

    diff_max_min = numbers[-1] - numbers[0]

    return [mean, median, most_frequent, diff_max_min]


if __name__ == "__main__":
    n = int(input())
    numbers = list()
    for _ in range(n):
        numbers.append(int(input()))

    answer = solution(numbers)
    print('\n'.join([str(number) for number in answer]))
