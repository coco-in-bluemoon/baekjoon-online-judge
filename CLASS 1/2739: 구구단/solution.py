def solution(n):
    lines = list()
    for multiplying_num in range(1, 10):
        line = '%d * %d = %d' % (n, multiplying_num, n * multiplying_num)
        lines.append(line)
    answer = '\n'.join(lines)
    return answer


if __name__ == "__main__":
    n = 2
    answer =\
        '2 * 1 = 2\n2 * 2 = 4\n2 * 3 = 6\n2 * 4 = 8\n2 * 5 = 10\n' +\
        '2 * 6 = 12\n2 * 7 = 14\n2 * 8 = 16\n2 * 9 = 18'
    assert solution(n) == answer

    n = int(input())
    answer = solution(n)
    print(answer)
