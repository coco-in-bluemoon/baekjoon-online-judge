from collections import defaultdict


def solution(word):
    frequency_dictionary = defaultdict(int)
    word = word.upper()
    for character in word:
        frequency_dictionary[character] += 1
    frequency_dictionary = sorted(
        frequency_dictionary.items(), key=lambda x: x[1], reverse=True
    )

    if len(frequency_dictionary) == 1:
        return frequency_dictionary[0][0]

    if frequency_dictionary[0][1] == frequency_dictionary[1][1]:
        return '?'

    return frequency_dictionary[0][0]


if __name__ == "__main__":
    word = 'Mississipi'
    assert solution(word) == '?'

    word = 'zZa'
    assert solution(word) == 'Z'

    word = input().strip()
    answer = solution(word)
    print(answer)
