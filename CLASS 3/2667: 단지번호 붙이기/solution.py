from collections import deque


def is_in_boundary(position, board):
    r, c = position
    R, C = len(board), len(board[0])

    return 0 <= r < R and 0 <= c < C


def solution(board):
    R, C = len(board), len(board[0])
    visited = [[False] * C for _ in range(R)]

    no = 0
    no_to_size = dict()
    for base_r in range(R):
        for base_c in range(C):
            if not board[base_r][base_c]:
                continue
            if visited[base_r][base_c]:
                continue

            no += 1
            size = 0
            queue = deque([(base_r, base_c)])

            while queue:
                r, c = queue.popleft()
                if visited[r][c]:
                    continue
                visited[r][c] = True
                size += 1

                for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    nr, nc = r + dr, c + dc

                    if not is_in_boundary((nr, nc), board):
                        continue
                    if not board[nr][nc]:
                        continue

                    queue.append((nr, nc))

            no_to_size[no] = size

    num_no = len(no_to_size)
    sizes = sorted(no_to_size.values())
    return num_no, sizes


if __name__ == "__main__":
    n = int(input())
    board = list()
    for _ in range(n):
        board.append(list(map(int, list(input()))))
    answer = solution(board)

    print(answer[0])
    print('\n'.join([str(size) for size in answer[1]]))
