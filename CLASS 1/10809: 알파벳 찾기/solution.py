def solution(word):
    ALPHABET_LENGTH = 26
    answer = [-1] * ALPHABET_LENGTH

    for index, alphabet in enumerate(word):
        alphabet_index = ord(alphabet) - ord('a')
        if answer[alphabet_index] == -1:
            answer[alphabet_index] = index

    return answer


if __name__ == "__main__":
    word = 'baekjoon'
    answer = [
        1, 0, -1, -1, 2, -1, -1, -1, -1,
        4, 3, -1, -1, 7, 5, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1
    ]
    assert solution(word) == answer

    word = input().strip()
    answer = solution(word)
    print(' '.join([str(num) for num in answer]))
