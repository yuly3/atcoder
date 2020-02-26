def solve():
    MOD = 10000
    N, K = map(int, input().split())
    A, B = [False] * N, [0] * N
    for _ in range(K):
        ai, bi = map(lambda x: int(x) - 1, input().split())
        A[ai] = True
        B[ai] = bi
    
    dp = [[[0] * 2 for _ in range(3)] for _ in range(N)]
    if A[0]:
        dp[0][B[0]][0] = 1
    else:
        for i in range(3):
            dp[0][i][0] = 1
    
    for i in range(1, N):
        if A[i]:
            for j in range(3):
                if j != B[i]:
                    dp[i][B[i]][0] += sum(dp[i - 1][j]) % MOD
            dp[i][B[i]][1] = dp[i - 1][B[i]][0]
        else:
            for j in range(3):
                for k in range(3):
                    if j != k:
                        dp[i][j][0] += sum(dp[i - 1][k]) % MOD
                dp[i][j][1] = dp[i - 1][j][0]
    ans = 0
    for i in range(3):
        ans += sum(dp[N - 1][i]) % MOD
    print(ans % MOD)


if __name__ == '__main__':
    solve()
