def draw_z(size, position, target):
    if size == 1:
        return (position == target, 1)

    base_r, base_c = position
    half_size = size // 2

    counter = 0
    matched = False
    if (target[0] >= (base_r + size)) or (target[1] >= (base_c + size)):
        counter = size ** 2
        return (matched, counter)

    for dr, dc in zip([0, 0, 1, 1], [0, 1, 0, 1]):
        r = base_r + (dr * half_size)
        c = base_c + (dc * half_size)

        matched, couter_partial = draw_z(half_size, (r, c), target)
        counter += couter_partial
        if matched:
            break

    return (matched, counter)


def solution(n, r, c):
    CORRECTION_FOR_ZERO_START = 1

    size = 2 ** n
    position = (0, 0)
    target = (r, c)

    _, answer = draw_z(size, position, target)
    return answer - CORRECTION_FOR_ZERO_START


if __name__ == "__main__":
    assert solution(2, 3, 1) == 11
    assert solution(3, 7, 7) == 63
    n, r, c = map(int, input().split())
    answer = solution(n, r, c)
    print(answer)
