from collections import deque


def in_boundary(position, board):
    r, c = position
    R, C = len(board), len(board[0])

    return 0 <= r < R and 0 <= c < C


def blocked(position, board):
    r, c = position
    return board[r][c] == 1


def cleaned(position, board):
    r, c = position
    for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        if not in_boundary((r+dr, c+dc), board):
            continue
        if not board[r+dr][c+dc]:
            return False
    return True


def solution(position, direction, board):
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    lefts = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    counter = 0
    stop = False
    r, c, d = position[0], position[1], direction
    while not stop:
        left = lefts[d]
        delta = deltas[d]

        if not board[r][c]:
            counter += 1
            board[r][c] = -1

        lr, lc = r+left[0], c+left[1]
        if cleaned((r, c), board):
            br, bc = r-delta[0], c-delta[1]
            if in_boundary((br, bc), board) and not blocked((br, bc), board):
                r, c, d = br, bc, d
            else:
                stop = True
        elif in_boundary((lr, lc), board) and not board[lr][lc]:
            r, c, d = lr, lc, (d-1) % 4
        else:
            r, c, d = r, c, (d-1) % 4

    return counter


if __name__ == "__main__":
    filename = './삼성 SW 역량 테스트 기출 문제/inputs/로봇 청소기.txt'
    f = open(filename, 'r')

    T = int(f.readline())
    f.readline()

    for t in range(T):
        N, M = map(int, f.readline().split())
        r, c, d = map(int, f.readline().split())
        board = [[0] * M for _ in range(N)]
        for n in range(N):
            board[n] = list(map(int, f.readline().split()))

        answer = int(f.readline())
        f.readline()

        my_answer = solution((r, c), d, board)
        assert my_answer == answer

    f.close()
