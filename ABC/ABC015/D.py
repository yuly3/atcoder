# Pythonだと実行制限時間超過
# PyPyだとメモリ制限超過
# Nimなら余裕

def solve():
    W = int(input())
    N, K = map(int, input().split())
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    
    dp = [[[0 for _ in range(W+1)] for _ in range(K+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(K):
            for k in range(W+1):
                if 0 <= k - A[i]:
                    dp[i+1][j+1][k] = max(dp[i][j+1][k], dp[i][j][k-A[i]] + B[i])
                else:
                    dp[i+1][j+1][k] = dp[i][j+1][k]
    print(dp[N][K][W])


if __name__ == '__main__':
    solve()
