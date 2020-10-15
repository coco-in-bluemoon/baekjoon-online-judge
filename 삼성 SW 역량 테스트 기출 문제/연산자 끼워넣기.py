from collections import deque
import math


def divide_cpp14(a, b):
    return a // b if (a * b) >= 0 else -1 * (abs(a) // abs(b))


def dfs(numbers, operators):
    if sum(operators) == 0:
        return [numbers[0], numbers[0]]

    max_number = -math.inf
    min_number = math.inf
    for idx, operator in enumerate(operators):
        if not operator:
            continue

        a = numbers.popleft()
        b = numbers.popleft()

        operators[idx] -= 1
        c = None
        if idx == 0:
            c = a + b
        elif idx == 1:
            c = a - b
        elif idx == 2:
            c = a * b
        elif idx == 3:
            c = divide_cpp14(a, b)

        numbers.appendleft(c)
        mx, mn = dfs(numbers, operators)
        operators[idx] += 1

        min_number = min(min_number, mn)
        max_number = max(max_number, mx)
        numbers.popleft()
        numbers.appendleft(b)
        numbers.appendleft(a)

    return [max_number, min_number]


def solution(numbers, operators):
    numbers = deque(numbers)
    answer = dfs(numbers, operators)
    return answer


if __name__ == "__main__":
    filename = './삼성 SW 역량 테스트 기출 문제/inputs/연산자 끼워넣기.txt'
    f = open(filename, 'r')
    T = int(f.readline())
    f.readline()
    for t in range(T):
        f.readline()
        numbers = list(map(int, f.readline().split()))
        operators = list(map(int, f.readline().split()))
        my_answer = solution(numbers, operators)
        answer = list(map(int, f.readline().split()))
        assert my_answer == answer
        f.readline()
    f.close()
