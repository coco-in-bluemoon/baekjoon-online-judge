from collections import deque


def is_in_boundary(position, board):
    r, c = position
    R = len(board)
    C = len(board[0])

    return 0 <= r < R and 0 <= c < C


def solution(board):
    R = len(board)
    C = len(board[0])

    visited = [[False] * C for _ in range(R)]
    queue = deque([])
    counter = 0

    for base_r in range(R):
        for base_c in range(C):
            if not board[base_r][base_c] or visited[base_r][base_c]:
                continue

            counter += 1

            queue.append((base_r, base_c))
            while queue:
                r, c = queue.popleft()
                if visited[r][c]:
                    continue
                visited[r][c] = True

                for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    nr, nc = r + dr, c + dc

                    if not is_in_boundary((nr, nc), board):
                        continue
                    if not board[nr][nc]:
                        continue

                    queue.append((nr, nc))

    return counter


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        C, R, n = map(int, input().split())
        board = [[0] * C for _ in range(R)]

        for _ in range(n):
            c, r = map(int, input().split())
            board[r][c] = 1

        answer = solution(board)
        print(answer)
