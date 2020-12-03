def solution(cards, numbers):
    card_to_freq = {number: 0 for number in numbers}

    for card in cards:
        if card not in card_to_freq:
            continue
        card_to_freq[card] += 1

    answer = list()
    for number in numbers:
        answer.append(card_to_freq[number])
    return answer


if __name__ == "__main__":
    n = int(input())
    cards = list(map(int, input().split()))
    m = int(input())
    numbers = list(map(int, input().split()))

    answer = solution(cards, numbers)
    print(' '.join(str(freq) for freq in answer))
