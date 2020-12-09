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


def solution(n, sentence):
    pattern = 'IO' * n + 'I'

    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    j = 0
    counter = 0
    for i in range(len(sentence)):
        while j > 0 and sentence[i] != pattern[j]:
            j = pi[j-1]

        if sentence[i] == pattern[j]:
            if j == len(pattern) - 1:
                counter += 1
                j = pi[j]
            else:
                j += 1

    return counter


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    sentence = input().strip()
    answer = solution(n, sentence)
    print(answer)
