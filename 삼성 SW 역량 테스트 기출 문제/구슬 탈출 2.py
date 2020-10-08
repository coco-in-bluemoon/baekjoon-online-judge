from collections import deque


def in_hole(pos, target):
    return pos[0] == target[0] and pos[1] == target[1]


def in_boundary(r, c, board):
    N = len(board)
    M = len(board[0])

    return 0 <= r < N and 0 <= c < M


def move_to_end(r, c, dr, dc, board):
    nr, nc = r + dr, c + dc
    counter = 0
    while in_boundary(nr, nc, board) and board[nr][nc] == '.':
        r, c = nr, nc
        nr, nc = r + dr, c + dc
        counter += 1

    if in_boundary(nr, nc, board) and board[nr][nc] == 'O':
        r, c = nr, nc

    return r, c, counter


def move_ball(rr, rc, br, bc, dr, dc, board):
    nrr, nrc, rcnt = move_to_end(rr, rc, dr, dc, board)
    nbr, nbc, bcnt = move_to_end(br, bc, dr, dc, board)

    if nrr == nbr and nrc == nbc:
        if board[nrr][nrc] != 'O':
            if rcnt > bcnt:
                nrr, nrc = nrr - dr, nrc - dc
            elif rcnt < bcnt:
                nbr, nbc = nbr - dr, nbc - dc

    return (nrr, nrc), (nbr, nbc)


def solution(board):
    N = len(board)
    M = len(board[0])

    red_pos = tuple()
    blue_pos = tuple()
    hole_pos = tuple()

    for r in range(N):
        for c in range(M):
            if board[r][c] == 'R':
                red_pos = (r, c)
                board[r][c] = '.'
            elif board[r][c] == 'B':
                blue_pos = (r, c)
                board[r][c] = '.'
            elif board[r][c] == 'O':
                hole_pos = (r, c)

    counter = 0
    queue = deque([(red_pos, blue_pos, counter)])
    visited = set()
    blue_hole = False
    while queue:
        item = queue.popleft()
        red_pos = item[0]
        blue_pos = item[1]
        counter = item[2]

        if (red_pos, blue_pos) in visited:
            continue
        visited.add((red_pos, blue_pos))

        # Break Case
        if counter > 10:
            return -1
        if in_hole(blue_pos, hole_pos):
            blue_hole = True
            continue
        if in_hole(red_pos, hole_pos) and not in_hole(blue_pos, hole_pos):
            blue_hole = False
            break

        # D - U - R - L
        for dr, dc in zip((1, -1, 0, 0), (0, 0, 1, -1)):
            rr, rc = red_pos
            br, bc = blue_pos

            next_red_pos, next_blue_pos =\
                move_ball(rr, rc, br, bc, dr, dc, board)
            item = (next_red_pos, next_blue_pos, counter+1)
            queue.append(item)

    rr, rc = red_pos
    answer = counter if board[rr][rc] == 'O' and not blue_hole else -1
    return answer


# File Input
if __name__ == "__main__":
    board, answer = None, None

    f = open('삼성 SW 역량 테스트 기출 문제/inputs/구슬 탈출 2.txt', 'r')
    T = int(f.readline())

    for t in range(T):
        N, M = map(lambda x: int(x), f.readline().split())
        board = [['.'] * M for _ in range(N)]
        for r in range(N):
            line = f.readline()
            line = line.strip()
            for c, val in enumerate(line):
                board[r][c] = val
        answer = int(f.readline())

        my_answer = solution(board)
        assert my_answer == answer
        print(f'{t+1:02} 번 문제 성공')

    f.close()

# Standard Input for Submission
# if __name__ == "__main__":
#     N, M = map(lambda x: int(x), input().split())
#     board = [list(input().rstrip()) for _ in range(N)]
#     answer = solution(board)
#     print(answer)
