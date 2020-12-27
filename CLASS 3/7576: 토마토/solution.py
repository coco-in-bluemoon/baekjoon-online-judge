from collections import deque


def is_in_boundary(position, board):
    r, c = position
    R, C = len(board), len(board[0])

    return 0 <= r < R and 0 <= c < C


def solution(board):
    STATE_RIPEN = 1
    STATE_NOT_RIPEN = 0
    STATE_EMPTY = -1
    
    R, C = len(board), len(board[0])

    queue = deque([])
    counter_not_ripen = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == STATE_NOT_RIPEN:
                counter_not_ripen += 1
            elif board[r][c] == STATE_RIPEN:
                queue.append((r, c))

    if not counter_not_ripen:
        return 0

    counter_iteration = 0
    while queue:
        counter_iteration += 1
        counter_ripen = len(queue)
        queue_next = deque([])

        for _ in range(counter_ripen):
            r, c = queue.popleft()

            for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                nr, nc = r + dr, c + dc

                if not is_in_boundary((nr, nc), board):
                    continue

                if board[nr][nc] == STATE_EMPTY:
                    continue
                elif board[nr][nc] == STATE_RIPEN:
                    continue
                elif board[nr][nc] == STATE_NOT_RIPEN:
                    counter_not_ripen -= 1
                    queue_next.append((nr, nc))
                    board[nr][nc] = STATE_RIPEN

        queue = queue_next

    return (counter_iteration - 1) if not counter_not_ripen else -1


if __name__ == "__main__":
    C, R = map(int, input().split())
    board = [[] * C for _ in range(R)]

    for r in range(R):
        board[r] = list(map(int, input().split()))

    answer = solution(board)
    print(answer)
