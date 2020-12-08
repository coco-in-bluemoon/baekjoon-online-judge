def is_all_same(position, size, board):
    base_r, base_c = position
    target = board[base_r][base_c]
    for dr in range(size):
        for dc in range(size):
            r, c = base_r + dr, base_c + dc
            if board[r][c] != target:
                return False
    return True


def divide_conquer_board(position, size, board):
    number_to_freq = {0: 0, 1: 0}
    if size == 1:
        r, c = position
        number_to_freq[board[r][c]] = 1
        return number_to_freq

    base_r, base_c = position
    if is_all_same(position, size, board):
        number_to_freq[board[base_r][base_c]] = 1
        return number_to_freq

    half_size = size // 2
    for dr in range(2):
        for dc in range(2):
            r = base_r + (dr * half_size)
            c = base_c + (dc * half_size)

            sub_answer = divide_conquer_board((r, c), half_size, board)
            for key, value in sub_answer.items():
                number_to_freq[key] += value

    return number_to_freq


def solution(board):
    position = (0, 0)
    size = len(board)
    answer = divide_conquer_board(position, size, board)
    return [answer[0], answer[1]]


if __name__ == "__main__":
    n = int(input())
    board = list()
    for _ in range(n):
        board.append(list(map(int, input().split())))
    answer = solution(board)
    print('{}\n{}'.format(answer[0], answer[1]))
