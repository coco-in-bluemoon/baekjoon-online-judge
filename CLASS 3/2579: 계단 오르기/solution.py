'''Note
dp[n] = max(dp[n-3] + arr[n-1] + arr[n], dp[n-2] + arr[n])
'''

def solution(stairs):
    if len(stairs) <= 2:
        return sum(stairs)

    dp = [0] * len(stairs)
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for index in range(3, len(stairs)):
        dp[index] = max(
            dp[index-2] + stairs[index],
            dp[index-3] + stairs[index-1] + stairs[index]
        )

    return dp[-1]


if __name__ == "__main__":
    n = int(input())
    stairs = list()
    for _ in range(n):
        stairs.append(int(input()))

    answer = solution(stairs)
    print(answer)
