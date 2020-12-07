def is_all_same(position, size, board):
    base_r, base_c = position

    target = board[base_r][base_c]
    for dr in range(size):
        for dc in range(size):
            r, c = base_r + dr, base_c + dc
            if board[r][c] != target:
                return False
    return True


def encode_board(position, size, board):
    if size == 1:
        r, c = position
        return str(board[r][c])

    base_r, base_c = position
    if is_all_same(position, size, board):
        return str(board[base_r][base_c])

    encoded = '('
    half_size = size // 2
    for dr in range(2):
        for dc in range(2):
            r = base_r + (dr * half_size)
            c = base_c + (dc * half_size)
            encoded += encode_board((r, c), half_size, board)
    encoded += ')'
    return encoded


def solution(board):
    answer = encode_board((0, 0), len(board), board)
    return answer


if __name__ == "__main__":
    n = int(input())
    board = list()
    for _ in range(n):
        board.append(list(input()))

    answer = solution(board)
    print(answer)
