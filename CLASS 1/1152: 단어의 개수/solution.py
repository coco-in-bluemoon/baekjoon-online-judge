def solution(sentence):
    return len(sentence.split())


if __name__ == "__main__":
    sentence = 'The Curious Case of Benjamin Button'
    assert solution(sentence) == 6

    sentence = input().strip()
    print(solution(sentence))
