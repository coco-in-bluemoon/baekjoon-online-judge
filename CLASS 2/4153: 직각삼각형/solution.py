def solution(a, b, c):
    a, b, c = sorted([a, b, c])

    if (a ** 2) + (b ** 2) == (c ** 2):
        return 'right'
    else:
        return 'wrong'


if __name__ == "__main__":
    while True:
        a, b, c = map(int, input().split())
        if (a, b, c) == (0, 0, 0):
            break
        answer = solution(a, b, c)
        print(answer)
