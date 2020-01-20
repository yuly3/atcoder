def solve():
    N, *p = map(float, open(0).read().split())
    N = int(N)

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] += dp[i][j] * p[i]
            dp[i + 1][j] += dp[i][j] * (1 - p[i])

    ans = 0
    for i in range((N + 1) // 2, N + 1):
        ans += dp[N][i]
    print(ans)


if __name__ == '__main__':
    solve()
