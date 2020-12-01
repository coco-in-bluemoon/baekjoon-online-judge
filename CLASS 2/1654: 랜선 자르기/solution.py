def solution(target, lines):
    left = 1
    right = max(lines)

    while left <= right:
        middle = (left + right) // 2

        counter = sum([line // middle for line in lines])

        if counter < target:
            right = middle - 1
        else:
            left = middle + 1

    return right


if __name__ == "__main__":
    target = 11
    lines = [802, 743, 457, 539]
    assert solution(target, lines) == 200

    n, target = map(int, input().split())
    lines = list()
    for _ in range(n):
        line = int(input())
        lines.append(line)
    answer = solution(target, lines)
    print(answer)
