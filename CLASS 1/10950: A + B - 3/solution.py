def solution(num_a, num_b):
    return num_a + num_b


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        num_a, num_b = map(int, input().split())
        answer = solution(num_a, num_b)
        print(answer)
