def solve():
    N, W = map(int, input().split())
    w, v = [0] * N, [0] * N
    for i in range(N):
        w[i], v[i] = map(int, input().split())
    
    V = sum(v)
    dp = [W + 1] * (V + 1)
    dp[0] = 0
    for i in range(N):
        for j in range(V, -1, -1):
            if dp[j] + w[i] <= W:
                dp[j + v[i]] = min(dp[j + v[i]], dp[j] + w[i])
    
    for i in range(V, -1, -1):
        if dp[i] <= W:
            print(i)
            exit()


if __name__ == '__main__':
    solve()
