def solve():
    N = int(input())
    a = list(map(int, input().split()))
    a += [a[-1], a[-1]]
    
    INF = 10 ** 10
    dp = [INF] * 100010
    dp[0] = 0
    
    for i in range(N):
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(a[i] - a[i + 1]))
        dp[i + 2] = dp[i] + abs(a[i] - a[i + 2])
    print(dp[N - 1])


if __name__ == '__main__':
    solve()
