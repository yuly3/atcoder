def solve():
    N, M, *a = map(int, open(0).read().split())
    ok = [True for _ in range(N+1)]
    for i in range(M):
        ok[a[i]] = False
    MOD = 1000000007

    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    for i in range(N):
        for j in range(i+1, min(N+1, i+3)):
            if ok[j]:
                dp[j] += dp[i]
                dp[j] %= MOD
    print(dp[N])


if __name__ == '__main__':
    solve()