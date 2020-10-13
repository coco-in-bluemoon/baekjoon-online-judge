def in_boundary(x, y, board):
    N, M = len(board), len(board[0])
    return 0 <= x < N and 0 <= y < M


def move_dice(command, x, y, dice, board):
    delta = {
        1: (0, 1),
        2: (0, -1),
        3: (-1, 0),
        4: (1, 0)
    }
    dx, dy = delta[command]
    nx, ny = x + dx, y + dy
    if not in_boundary(nx, ny, board):
        return x, y, None

    if command == 1:
        temp = dice[1][0]
        dice[1] = [dice[1][1], dice[1][2], dice[3][1]]
        dice[3][1] = temp
    elif command == 2:
        temp = dice[1][2]
        dice[1] = [dice[3][1], dice[1][0], dice[1][1]]
        dice[3][1] = temp
    elif command == 3:
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = temp
    elif command == 4:
        temp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = temp

    bottom = dice[1][1]
    target = board[nx][ny]

    if not target:
        board[nx][ny] = bottom
    else:
        dice[1][1] = board[nx][ny]
        board[nx][ny] = 0

    return nx, ny, dice[3][1]


def solution(board, x, y, commands):
    dice = [
        [None, 0, None],
        [0, 0, 0],
        [None, 0, None],
        [None, 0, None]
    ]

    answer = list()
    for command in commands:
        nx, ny, top = move_dice(command, x, y, dice, board)
        if top is not None:
            x, y = nx, ny
            answer.append(top)

    return answer


if __name__ == "__main__":
    filename = './삼성 SW 역량 테스트 기출 문제/inputs/주사위 굴리기.txt'
    f = open(filename, 'r')
    T = int(f.readline())
    f.readline()

    for t in range(T):
        N, M, x, y, K = map(int, f.readline().split())
        board = [[0] * M for _ in range(N)]
        for n in range(N):
            line = f.readline().split()
            for m, val in enumerate(line):
                board[n][m] = int(val)
        commands = list(map(int, f.readline().split()))
        answer = list(map(int, f.readline().split()))
        f.readline()

        my_answer = solution(board, x, y, commands)
        assert my_answer == answer
