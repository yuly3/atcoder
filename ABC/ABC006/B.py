def solve():
    n = int(input())
    dp = [0] * (10 ** 6)
    dp[2] = 1
    MOD = 10007
    
    for i in range(3, n):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD
    print(dp[n - 1])


if __name__ == '__main__':
    solve()
