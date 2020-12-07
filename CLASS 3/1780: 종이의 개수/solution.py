def is_all_same(position, size, board):
    base_r, base_c = position
    target = board[base_r][base_c]
    for dr in range(size):
        for dc in range(size):
            r = base_r + dr
            c = base_c + dc

            if board[r][c] != target:
                return False

    return True


def count_block_recursively(position, size, board):
    counter = {-1: 0, 0: 0, 1: 0}

    if size == 1:
        r, c = position
        counter[board[r][c]] = 1
        return counter

    base_r, base_c = position
    if is_all_same(position, size, board):
        counter[board[base_r][base_c]] = 1
        return counter

    third_size = size // 3
    for dr in range(3):
        for dc in range(3):
            r = base_r + (dr * third_size)
            c = base_c + (dc * third_size)

            counter_part = count_block_recursively((r, c), third_size, board)
            for key, value in counter_part.items():
                counter[key] += value

    return counter


def solution(board):
    answer = count_block_recursively((0, 0), len(board), board)
    return [answer[-1], answer[0], answer[1]]


if __name__ == "__main__":
    size = int(input())
    board = list()
    for _ in range(size):
        board.append(list(map(int, input().split())))

    answer = solution(board)
    print('\n'.join([str(number) for number in answer]))
