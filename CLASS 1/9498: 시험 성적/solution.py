def solution(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


if __name__ == "__main__":
    assert solution(100) == 'A'

    score = int(input())
    answer = solution(score)
    print(answer)
