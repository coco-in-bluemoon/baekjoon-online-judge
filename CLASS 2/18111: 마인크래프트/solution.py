'''
1. 이분 탐색으로 수행한 경우 제대로 된 답을 찾지 못할 수 있다.
2. 모든 경우의 수 탐색을 파이썬으로 수행하면 시간 초과 발생 → 행렬보다 {높이: 개수}의 딕셔너리를 활용하는 것이 낫다.
'''
from collections import Counter


def solution(board, inventory):
    HIGHEST = 256
    answer_height = None
    answer_second = None

    heights = sum(board, [])
    total = sum(heights)
    length = len(heights)

    counter_heights = dict(Counter(heights))

    for target_height in range(HIGHEST+1):
        if (total + inventory) < (target_height * length):
            break

        second = 0
        for height, counter in counter_heights.items():
            height_diff = abs(target_height - height)
            if height < target_height:
                second += (height_diff * counter)
            elif height > target_height:
                second += (2 * height_diff * counter)

        if answer_height is None and answer_second is None:
            answer_height = target_height
            answer_second = second
        elif (second < answer_second) or\
                (second == answer_second and target_height > answer_height):
            answer_height = target_height
            answer_second = second

    return [answer_second, answer_height]


if __name__ == "__main__":
    row, col, inventory = map(int, input().split())
    board = [0] * row
    for r in range(row):
        board[r] = list(map(int, input().split()))

    answer = solution(board, inventory)
    print('{:} {:}'.format(answer[0], answer[1]))

    # 이분 탐색이 안되는 반례
    board = [
        [30, 21, 48, 55, 1, 1, 4],
        [0, 0, 0, 0, 0, 0, 0],
        [15, 4, 4, 4, 4, 4, 8],
        [20, 40, 60, 10, 20, 30, 2],
        [1, 1, 1, 1, 1, 1, 9],
        [24, 12, 33, 7, 14, 25, 3],
        [3, 3, 3, 3, 3, 3, 32]
    ]
    inventory = 6000
    assert solution(board, inventory) == [879, 10]
