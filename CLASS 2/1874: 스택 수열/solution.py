from collections import deque


def solution(sequence):
    stack = deque([])

    operations = ''
    current_number = 1

    for number in sequence:
        if number >= current_number:
            while current_number <= number:
                stack.append(current_number)
                operations += '+'
                current_number += 1
            stack.pop()
            operations += '-'
        else:
            if stack and stack[-1] == number:
                stack.pop()
                operations += '-'
            else:
                operations = None
                break

    return operations


if __name__ == "__main__":
    n = int(input())
    sequence = list()
    for _ in range(n):
        number = int(input())
        sequence.append(number)

    answer = solution(sequence)
    print('\n'.join(answer) if answer else 'NO')
