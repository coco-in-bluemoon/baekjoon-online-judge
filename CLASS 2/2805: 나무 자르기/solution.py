def solution(target, heights):
    left = 0
    right = max(heights)

    while left <= right:
        middle = (left + right) // 2

        sum_height = 0
        for height in heights:
            sum_height += max(height - middle, 0)

        if sum_height >= target:
            left = middle + 1
        elif sum_height < target:
            right = middle - 1

    return right


if __name__ == "__main__":
    n, target = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = solution(target, heights)
    print(answer)
