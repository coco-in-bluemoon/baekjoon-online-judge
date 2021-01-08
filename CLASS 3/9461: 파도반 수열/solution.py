def solution(value):
    dp = [1, 1, 1, 2, 2]

    for num in range(5, value):
        dp.append(dp[num-1] + dp[num-5])

    return dp[value-1]


if __name__ == "__main__":
    num_test = int(input())
    for _ in range(num_test):
        value = int(input())
        answer = solution(value)
        print(answer)
