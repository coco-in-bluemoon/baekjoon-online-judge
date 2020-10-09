from collections import deque


def move(start, end, row, col, delta, board):
    N = len(board)
    board_copy = [[0] * N for _ in range(N)]

    # Up and Down
    if row:
        for c in range(N):
            board_copy[start][c] = board[start][c]
            idx = start
            for r in range(start, end, delta):
                a = board_copy[idx][c]
                b = board[r+delta][c]

                if not b:
                    continue

                if a == b:
                    board_copy[idx][c] = a + b
                    idx += delta
                elif a == 0:
                    board_copy[idx][c] = b
                else:
                    idx += delta
                    board_copy[idx][c] = b
    # Left or Right
    elif col:
        for r in range(N):
            board_copy[r][start] = board[r][start]
            idx = start
            for c in range(start, end, delta):
                a = board_copy[r][idx]
                b = board[r][c+delta]

                if not b:
                    continue

                if a == b:
                    board_copy[r][idx] = a + b
                    idx += delta
                elif a == 0:
                    board_copy[r][idx] = b
                else:
                    idx += delta
                    board_copy[r][idx] = b

    return board_copy, max(sum(board_copy, []))


def solution(board):
    N = len(board)

    answer = max(sum(board, []))
    queue = deque([(board, 0, answer)])

    # left, right, up, down
    parameters = [
        (0, N-1, 0, 1, 1),
        (N-1, 0, 0, 1, -1),
        (0, N-1, 1, 0, 1),
        (N-1, 0, 1, 0, -1)
    ]

    visited = set()
    while queue:
        board, depth, number = queue.popleft()
        if depth > 5:
            continue

        board_id = ''.join([str(val) for val in sum(board, [])])
        if board_id in visited:
            continue
        visited.add(board_id)
        answer = max(answer, number)

        for parameter in parameters:
            start, end, row, col, delta = parameter
            moved, nb = move(start, end, row, col, delta, board)

            board_id = ''.join([str(val) for val in sum(moved, [])])
            if board_id in visited:
                continue

            queue.append((moved, depth+1, nb))

    return answer


# File Input
if __name__ == "__main__":
    filename = '삼성 SW 역량 테스트 기출 문제/inputs/2048 easy.txt'
    board = None
    with open(filename, 'r', encoding='utf-8') as f:
        T = int(f.readline())
        for t in range(T):
            N = int(f.readline())
            board = [
                [int(val) for val in f.readline().split()] for _ in range(N)
            ]
            answer = int(f.readline())
            assert solution(board) == answer


# Standard Input
# if __name__ == "__main__":
#     N = int(input())
#     board = [
#         [int(val) for val in input().rstrip().split()] for _ in range(N)
#     ]
#     answer = solution(board)
#     print(answer)
