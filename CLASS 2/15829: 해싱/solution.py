def solution(word):
    R = 31
    M = 1234567891

    hash_value = 0
    for idx, character in enumerate(word):
        character_value = ord(character) - ord('a') + 1
        hash_value += (character_value * (R ** idx))
        hash_value %= M

    return hash_value


if __name__ == "__main__":
    n = int(input())
    word = input().strip()
    answer = solution(word)
    print(answer)
