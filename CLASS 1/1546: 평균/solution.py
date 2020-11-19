def solution(scores):
    maximum_score = max(scores)
    modified_scores = [score/maximum_score * 100 for score in scores]
    return sum(modified_scores) / len(modified_scores)


if __name__ == "__main__":
    scores = [40, 80, 60]
    assert solution(scores) == 75.0

    scores = [1, 100, 100, 100]
    assert solution(scores) == 75.25

    N = int(input())
    scores = list(map(int, input().split()))
    answer = solution(scores)
    print(answer)
