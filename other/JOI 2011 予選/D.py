def solve():
    N, *A = map(int, open(0).read().split())
    
    dp = [[0] * 21 for _ in range(N - 1)]
    dp[0][A[0]] = 1
    
    for i in range(1, N - 1):
        for j in range(21):
            if j + A[i] <= 20:
                dp[i][j + A[i]] += dp[i - 1][j]
            if 0 <= j - A[i]:
                dp[i][j - A[i]] += dp[i - 1][j]
    print(dp[N - 2][A[-1]])


if __name__ == '__main__':
    solve()
