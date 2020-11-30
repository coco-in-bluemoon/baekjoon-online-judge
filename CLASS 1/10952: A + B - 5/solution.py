import sys


def solution(num_a, num_b):
    return num_a + num_b


if __name__ == "__main__":
    for line in sys.stdin:
        num_a, num_b = map(int, line.split())
        if (num_a, num_b) == (0, 0):
            break
        answer = solution(num_a, num_b)
        print(answer)
