def solution(a, b):
    if a > b:
        return '>'
    if a < b:
        return '<'
    if a == b:
        return '=='


if __name__ == "__main__":
    assert solution(1, 2) == '<'
    assert solution(10, 1) == '>'
    assert solution(5, 5) == '=='

    a, b = map(int, input().split())
    answer = solution(a, b)
    print(answer)
