def solve():
    N, M = map(int, input().split())
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = int(input())
    C = [0] * (M + 1)
    for i in range(1, M + 1):
        C[i] = int(input())
    
    dp = [[10 ** 10] * (N + 1) for _ in range(M + 1)]
    for i in range(M + 1):
        dp[i][0] = 0
    
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j], dp[i - 1][j - 1] + D[j] * C[i])
    print(dp[M][N])


if __name__ == '__main__':
    solve()
