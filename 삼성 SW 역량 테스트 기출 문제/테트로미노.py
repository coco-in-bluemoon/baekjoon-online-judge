def match_tetromino(board, shape):
    N = len(board)
    M = len(board[0])

    R = len(shape)
    C = len(shape[0])

    if N < R:
        return 0

    summation = 0
    for br in range(N-R+1):
        for bc in range(M-C+1):
            temp = 0
            for r in range(R):
                for c in range(C):
                    temp += (board[br+r][bc+c] * shape[r][c])
            summation = max(summation, temp)

    return summation


def solution(board):
    tetromino = [
        [[1, 1, 1, 1]],
        [[1, 1], [1, 1]],
        [[1, 1, 1], [1, 0, 0]],
        [[1, 1, 1], [0, 1, 0]],
        [[1, 1, 1], [0, 0, 1]],
        [[1, 0, 0], [1, 1, 1]],
        [[0, 1, 0], [1, 1, 1]],
        [[0, 0, 1], [1, 1, 1]],
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1, 1], [1, 1, 0]],
        [[1, 1], [1, 0], [1, 0]],
        [[1, 0], [1, 1], [1, 0]],
        [[1, 0], [1, 0], [1, 1]],
        [[1, 1], [0, 1], [0, 1]],
        [[0, 1], [1, 1], [0, 1]],
        [[0, 1], [0, 1], [1, 1]],
        [[1, 0], [1, 1], [0, 1]],
        [[0, 1], [1, 1], [1, 0]],
        [[1], [1], [1], [1]],
    ]

    answer = 0
    for idx, shape in enumerate(tetromino):
        temp = match_tetromino(board, shape)
        answer = max(answer, temp)
    return answer


if __name__ == "__main__":
    filename = '삼성 SW 역량 테스트 기출 문제/inputs/테트로미노.txt'
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
        assert my_answer == answer
        f.readline()
    f.close()
