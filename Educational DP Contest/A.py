def solve():
    N, *h = map(int, open(0).read().split())
    h += [h[-1]]
    
    dp = [10 ** 10] * (N + 1)
    dp[0] = 0
    for i in range(N - 1):
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
        dp[i + 2] = dp[i] + abs(h[i] - h[i + 2])
    print(dp[N - 1])


if __name__ == '__main__':
    solve()
