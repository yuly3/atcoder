import sys
read = sys.stdin.readline


def solve():
    N = int(read())
    P = [0] * N
    for i in range(N):
        P[i] = int(read())
    
    dp = [0] * (N + 1)
    ans = 0
    for i in range(N):
        p = P[i]
        dp[p] = dp[p - 1] + 1
        ans = max(ans, dp[p])
    print(N - ans)


if __name__ == '__main__':
    solve()
