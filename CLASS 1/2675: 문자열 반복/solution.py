def solution(n, word):
    answer = ''
    for character in word:
        answer += (character * n)
    return answer


if __name__ == "__main__":
    assert solution(3, 'ABC') == 'AAABBBCCC'
    assert solution(5, '/HTP') == '/////HHHHHTTTTTPPPPP'

    num_testcase = int(input())
    for _ in range(num_testcase):
        n, word = input().split()
        n = int(n)

        answer = solution(n, word)
        print(answer)
