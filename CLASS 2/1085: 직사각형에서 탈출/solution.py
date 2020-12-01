def solution(x, y, w, h):
    return min(abs(w - x), abs(h - y), x, y)


if __name__ == "__main__":
    x, y, w, h = map(int, input().split())
    answer = solution(x, y, w, h)
    print(answer)
