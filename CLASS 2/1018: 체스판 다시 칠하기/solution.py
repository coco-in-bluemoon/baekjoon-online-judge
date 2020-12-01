import math


def count_error_block(position, board):
    PARTITION_SIZE = 8
    base_r, base_c = position

    block_symbol = board[base_r][base_c]
    counter = 0
    for dr in range(PARTITION_SIZE):
        for dc in range(PARTITION_SIZE):
            r = base_r + dr
            c = base_c + dc

            if board[r][c] != block_symbol:
                counter += 1
            block_symbol = 'W' if block_symbol == 'B' else 'B'

        block_symbol = 'W' if block_symbol == 'B' else 'B'

    return min(counter, PARTITION_SIZE * PARTITION_SIZE - counter)


def solution(board):
    PARTITION_SIZE = 8
    R = len(board)
    C = len(board[0])

    answer = math.inf
    for base_r in range(R-PARTITION_SIZE+1):
        for base_c in range(C-PARTITION_SIZE+1):
            num_error_block = count_error_block((base_r, base_c), board)
            answer = min(answer, num_error_block)
    return answer


if __name__ == "__main__":
    board = [
        'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
        'BWBBBWBW', 'WBWBWBWB', 'BWBWBWBW',
        'WBWBWBWB', 'BWBWBWBW'
    ]
    assert solution(board) == 1

    board = [
        'BBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
        'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
        'WBWBWBWB', 'BWBWBWBW'
    ]
    assert solution(board) == 1

    board = [
        'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB',
        'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB',
        'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB',
        'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB',
        'WWWWWWWWWWBWB', 'WWWWWWWWWWBWB'
    ]
    assert solution(board) == 12

    board = [
        'WBWBWBWB', 'WBWBWBWB', 'WBWBWBWB',
        'WBWBWBWB', 'WBWBWBWB', 'WBWBWBWB',
        'WBWBWBWB', 'WBWBWBWB'
    ]
    assert solution(board) == 32

    board = [
        'WWBBWWWBBW', 'WBBWBWWWWB', 'WBWBWWBBWW',
        'WBBBBBBBWW', 'WBBWWWBWWW', 'WBBBBBWWBB',
        'WWBWWBWWBB', 'BWWBBWWWBB', 'BBWBBBBBWB',
        'WWWBBBWWWB'
    ]
    assert solution(board) == 29

    board = [
        'WWWWWWWW', 'WWWWWWWW', 'WWWWWWWW', 
        'WWWWWWWW', 'WWWWWWWW', 'WWWWWWWW',
        'WWWWWWWW', 'WWWWWWWB'
    ]
    assert solution(board) == 31

    board = [
        'WWWWWWWB', 'WBBBBBBB', 'WBWBWBWB',
        'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
        'WBWBWBWB', 'BWBWBWBW'
    ]
    assert solution(board) == 8

    N, M = map(int, input().split())
    board = list()
    for _ in range(N):
        line = input().strip()
        board.append(line)
    answer = solution(board)
    print(answer)
