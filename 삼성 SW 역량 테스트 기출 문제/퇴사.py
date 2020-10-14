def solution(times, prices):
    N = len(times)
    dp = [0] * N

    price_mx = 0
    for idx, (t, p) in enumerate(zip(times, prices)):
        if idx+t > N:
            price_mx = max(price_mx, dp[idx])
            continue
        dp[idx+t-1] = max(price_mx+p, dp[idx+t-1])
        price_mx = max(price_mx, dp[idx])

    return max(dp)


if __name__ == "__main__":
    filename = './삼성 SW 역량 테스트 기출 문제/inputs/퇴사.txt'
    f = open(filename, 'r')

    T = int(f.readline())
    f.readline()
    for t in range(T):
        N = int(f.readline())
        times = [0] * N
        prices = [0] * N

        for n in range(N):
            t, p = map(int, f.readline().split())
            times[n] = t
            prices[n] = p

        my_answer = solution(times, prices)
        answer = int(f.readline())
        f.readline()

        assert my_answer == answer

    f.close()
