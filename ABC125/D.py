def solve():
    N, *A = map(int, open(0).read().split())
    
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    dp[0][1] = -10**15
    for i in range(N):
        dp[i+1][0] = max(dp[i][0]+A[i], dp[i][1]-A[i])
        dp[i+1][1] = max(dp[i][0]-A[i], dp[i][1]+A[i])
    print(dp[N][0])


if __name__ == '__main__':
    solve()