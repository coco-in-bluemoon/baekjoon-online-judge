from collections import deque


def in_boundary(pos, board):
    R = len(board)
    C = len(board[0])

    return 0 <= pos[0] < R and 0 <= pos[1] < C


def blocked(pos, board):
    return board[pos[0]][pos[1]] == 1


def simulate_virus(virus, board):
    queue = deque(virus)
    visited = set()
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nr, nc = r+dr, c+dc
            if not in_boundary((nr, nc), board):
                continue
            if blocked((nr, nc), board):
                continue
            if (nr, nc) in visited:
                continue
            board[nr][nc] = 2
            queue.append((nr, nc))

    counter = sum(board, []).count(0)
    visited = visited - set(virus)
    for r, c in visited:
        board[r][c] = 0
    return counter


def block_virus(virus, board, block, counter):
    R = len(board)
    C = len(board[0])

    if counter == 3:
        answer = simulate_virus(virus, board)
        return answer

    answer = 0
    for r in range(R):
        for c in range(C):
            if board[r][c]:
                continue

            block_id = r * C + c
            if block > block_id:
                continue
            board[r][c] = 1
            temp = block_virus(virus, board, block_id, counter+1)
            answer = max(answer, temp)
            board[r][c] = 0
    return answer


def solution(board):
    R = len(board)
    C = len(board[0])

    virus = list()
    for r in range(R):
        for c in range(C):
            if board[r][c] == 2:
                virus.append((r, c))

    answer = block_virus(virus, board, -1, 0)
    return answer


if __name__ == "__main__":
    filename = '삼성 SW 역량 테스트 기출 문제/inputs/연구소.txt'
    f = open(filename, 'r')
    T = int(f.readline())
    f.readline()

    for t in range(T):
        N, M = map(int, f.readline().split())
        board = [[0] * M for _ in range(N)]
        for n in range(N):
            board[n] = list(map(int, f.readline().split()))

        my_answer = solution(board)
        answer = int(f.readline())

        try:
            assert my_answer == answer
            print(f'{t+1}번 문제 통과')
        except AssertionError:
            print(f'{t+1}번 문제 실패 MY: {my_answer} ANS: {answer}')
        f.readline()
    f.close()
