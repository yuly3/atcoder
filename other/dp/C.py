def solve():
    N, *abc = map(int, open(0).read().split())
    a = abc[::3]
    b = abc[1::3]
    c = abc[2::3]
    
    dp = [[10 ** 10] * 3 for _ in range(N)]
    dp[0][0], dp[0][1], dp[0][2] = a[0], b[0], c[0]
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a[i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + b[i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + c[i]
    print(max(dp[N - 1]))


if __name__ == '__main__':
    solve()
