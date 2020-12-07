from collections import deque


def is_in_boundary(position, board):
    r, c = position
    R, C = len(board), len(board[0])

    return 0 <= r < R and 0 <= c < C


def solution(board):
    BLOCK_SYMBOL = '0'
    R, C = len(board), len(board[0])

    counter = 0
    queue = deque([(0, 0, 1)])
    visited = [[False] * C for _ in range(R)]
    while queue:
        r, c, counter = queue.popleft()

        if visited[r][c]:
            continue
        visited[r][c] = True

        if (r, c) == (R-1, C-1):
            break

        for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nr, nc = r + dr, c + dc

            if not is_in_boundary((nr, nc), board):
                continue

            if board[nr][nc] == BLOCK_SYMBOL:
                continue

            if visited[nr][nc]:
                continue

            queue.append((nr, nc, counter + 1))

    return counter


if __name__ == "__main__":
    r, c = map(int, input().split())
    board = list()
    for _ in range(r):
        board.append(list(input()))
    answer = solution(board)
    print(answer)
