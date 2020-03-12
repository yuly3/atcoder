def solve():
    D, N = map(int, input().split())
    T = [0] * D
    for i in range(D):
        T[i] = int(input())
    A, B, C = [0] * N, [0] * N, [0] * N
    for i in range(N):
        A[i], B[i], C[i] = map(int, input().split())
    
    dp = [[0] * N for _ in range(D)]
    for i in range(N):
        if A[i] <= T[0] <= B[i]:
            continue
        else:
            dp[0][i] = -1
    
    for i in range(1, D):
        for j in range(N):
            if dp[i - 1][j] == -1:
                continue
            for k in range(N):
                if A[k] <= T[i] <= B[k]:
                    dp[i][k] = max(dp[i][k], dp[i - 1][j] + abs(C[j] - C[k]))
                else:
                    dp[i][k] = -1
    print(max(dp[D - 1]))


if __name__ == '__main__':
    solve()
