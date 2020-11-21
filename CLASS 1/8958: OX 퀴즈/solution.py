def solution(ox_mark):
    total_score = 0
    score = 1

    for mark in ox_mark:
        if mark == 'O':
            total_score += score
            score += 1
        else:
            score = 1

    return total_score


if __name__ == "__main__":
    ox_mark = 'OOXXOXXOOO'
    assert solution(ox_mark) == 10

    ox_mark = 'OOXXOOXXOO'
    assert solution(ox_mark) == 9

    ox_mark = 'OXOXOXOXOXOXOX'
    assert solution(ox_mark) == 7

    ox_mark = 'OOOOOOOOOO'
    assert solution(ox_mark) == 55

    ox_mark = 'OOOOXOOOOXOOOOX'
    assert solution(ox_mark) == 30

    num_case = int(input())
    for _ in range(num_case):
        ox_mark = input().strip()
        answer = solution(ox_mark)
        print(answer)
