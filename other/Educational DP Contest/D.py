def solve():
    N, W = map(int, input().split())
    w, v = [0] * N, [0] * N
    for i in range(N):
        w[i], v[i] = map(int, input().split())
    
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W - w[i], -1, -1):
            dp[j + w[i]] = max(dp[j + w[i]], dp[j] + v[i])
    print(dp[W])


if __name__ == '__main__':
    solve()
