def solve():
    MOD = 10**9+7
    N = int(input())
    
    dp = [[0 for _ in range(4)] for _ in range(N+1)]
    dp[1] = [1, 1, 1, 1]
    
    for i in range(2, N+1):
        for j in range(4):
            dp[i][j] += sum(dp[i-1])
            dp[i][j] %= MOD
        dp[i][1] -= dp[i-2][0] + dp[i-2][2]
        dp[i][2] -= dp[i-2][0]
        if 3 <= i:
            dp[i][1] -= dp[i-3][0] * 3
            dp[i][2] += dp[i-3][2]
    
    ans = sum(dp[N]) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
