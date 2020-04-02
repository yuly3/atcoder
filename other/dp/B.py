def solve():
    N, K, *h = map(int, open(0).read().split())
    h += [h[-1]] * K
    
    dp = [10 ** 10] * (N + K)
    dp[0] = 0
    for i in range(N - 1):
        for j in range(1, K + 1):
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]))
    print(dp[N - 1])


if __name__ == '__main__':
    solve()
