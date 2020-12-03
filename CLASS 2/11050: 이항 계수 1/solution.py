def solution(n, k):
    dp = [[1] * (n+1) for _ in range(n+1)]

    for dp_n in range(1, n+1):
        for dp_k in range(1, dp_n):
            dp[dp_n][dp_k] = dp[dp_n-1][dp_k-1] + dp[dp_n-1][dp_k]

    return dp[n][k]


if __name__ == "__main__":
    n, k = map(int, input().split())
    answer = solution(n, k)
    print(answer)
