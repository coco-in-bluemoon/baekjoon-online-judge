def solution(words):
    words = list(set(words))
    words = sorted(words, key=lambda word: (len(word), word))
    return list(words)


if __name__ == "__main__":
    N = int(input())
    words = list()
    for _ in range(N):
        word = input().strip()
        words.append(word)

    answer = solution(words)
    print('\n'.join(answer))
