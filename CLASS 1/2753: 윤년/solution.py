def solution(year):
    return 1 if (not year % 4 and year % 100) or (not year % 400) else 0


if __name__ == "__main__":
    year = 2000
    assert solution(year) == 1

    year = 1999
    assert solution(year) == 0

    year = int(input())
    answer = solution(year)
    print(answer)
