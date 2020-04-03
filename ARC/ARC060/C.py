import sys

rl = sys.stdin.readline


def solve():
    N, A = map(int, rl().split())
    x = list(map(int, rl().split()))
    
    y = [xi - A for xi in x]
    dp = [[0] * 5001 for _ in range(N + 1)]
    dp[0][2500] = 1
    
    for i in range(N):
        for j in range(5001):
            if 0 <= j - y[i] < 5001:
                dp[i + 1][j] = dp[i][j] + dp[i][j - y[i]]
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][2500] - 1)


if __name__ == '__main__':
    solve()
