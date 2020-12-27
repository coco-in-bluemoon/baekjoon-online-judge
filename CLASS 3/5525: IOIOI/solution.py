'''Note
1. 정규표현식의 Lookahead Assertsion (?=())을 사용. → 시간 초과
2. KMP 알고리즘 사용 필수
'''


import re


def solution_overtime(n, sentence):
    pattern = 'IO' * n + 'I'
    pattern = r'(?=(' + pattern + '))'
    matched = re.findall(pattern, sentence)
    return len(matched)


def calculate_prefix_table(pattern):
    prefix_table = [0] * len(pattern)

    i, j = 1, 0
    while i < len(pattern):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j
        i += 1

    return prefix_table


def apply_kmp_algorithm(sentence, pattern, prefix_table):
    i, j = 0, 0
    counter = 0
    while i < len(sentence):
        while j > 0 and sentence[i] != pattern[j]:
            j = prefix_table[j-1]
        if sentence[i] == pattern[j]:
            if j == len(pattern) - 1:
                counter += 1
                j = prefix_table[j]
            else:
                j += 1
        i += 1
    return counter


def solution(n, sentence):
    pattern = 'O'.join(['I'] * (n + 1))
    prefix_table = calculate_prefix_table(pattern)

    counter = apply_kmp_algorithm(sentence, pattern, prefix_table)
    return counter


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    sentence = input().strip()
    answer = solution(n, sentence)
    print(answer)
