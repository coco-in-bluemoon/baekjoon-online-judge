def solution(a, b):
    return a / b


if __name__ == "__main__":
    a, b = map(int, input().split())
    answer = solution(a, b)
    print(answer)
