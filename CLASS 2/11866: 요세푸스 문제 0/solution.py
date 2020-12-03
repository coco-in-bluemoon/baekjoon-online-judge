def solution(n, k):
    numbers = list(range(1, n+1))
    target_index = k-1
    sequence = list()

    while len(numbers) > 1:
        target_number = numbers[target_index]
        sequence.append(target_number)

        numbers.pop(target_index)
        target_index += (k-1)
        target_index = target_index % len(numbers)

    sequence.extend(numbers)

    return sequence


if __name__ == "__main__":
    n, k = map(int, input().split())
    answer = solution(n, k)
    print('<' + ', '.join(str(number) for number in answer) + '>')
