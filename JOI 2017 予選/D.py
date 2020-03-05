def solve():
    N, M = map(int, input().split())
    A = [int(input()) - 1 for _ in range(N)]
    
    cumsum = [[0] * M for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            cumsum[i + 1][j] = cumsum[i][j] + (A[i] == j)
    
    INF = 10 ** 6
    dp = [INF] * (2 ** M)
    dp[0] = 0
    
    for S in range(2 ** M):
        placed = sum(cumsum[N][kind] for kind in range(M) if (S >> kind) & 1)
        for i in range(M):
            if (S >> i) & 1:
                continue
            cost = cumsum[N][i] - (cumsum[placed + cumsum[N][i]][i] - cumsum[placed][i])
            dp[(1 << i) | S] = min(dp[(1 << i) | S], dp[S] + cost)
    print(dp[2 ** M - 1])


if __name__ == '__main__':
    solve()
