from collections import deque


def is_in_boundary(position, board):
    h, r, c = position
    H, R, C = len(board), len(board[0]), len(board[0][0])

    return 0 <= h < H and 0 <= r < R and 0 <= c < C


def solution(board):
    STATE_NOT_RIPEN = 0
    STATE_RIPEN = 1
    STATE_EMPTY = -1

    H, R, C = len(board), len(board[0]), len(board[0][0])

    queue = deque([])
    counter_not_ripen = 0
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if board[h][r][c] == STATE_NOT_RIPEN:
                    counter_not_ripen += 1
                elif board[h][r][c] == STATE_RIPEN:
                    queue.append((h, r, c))

    if not counter_not_ripen:
        return 0

    counter_iter = 0
    while queue:
        counter_iter += 1
        counter_ripen = len(queue)
        queue_next = deque([])

        for _ in range(counter_ripen):
            h, r, c = queue.popleft()
            for dh, dr, dc in zip([0, 0, 0, 0, -1, 1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]):
                nh, nr, nc = h + dh, r + dr, c + dc

                if not is_in_boundary((nh, nr, nc), board):
                    continue

                if board[nh][nr][nc] == STATE_EMPTY:
                    continue

                if board[nh][nr][nc] == STATE_RIPEN:
                    continue

                if board[nh][nr][nc] == STATE_NOT_RIPEN:
                    queue_next.append((nh, nr, nc))
                    board[nh][nr][nc] = STATE_RIPEN
                    counter_not_ripen -= 1
            
        queue = deque(queue_next)

    return (counter_iter - 1) if not counter_not_ripen else -1


if __name__ == "__main__":
    C, R, H = map(int, input().split())
    board = [[[] * C for _ in range(R)] for _ in range(H)]

    for h in range(H):
        for r in range(R):
            board[h][r] = list(map(int, input().split()))

    answer = solution(board)
    print(answer)
