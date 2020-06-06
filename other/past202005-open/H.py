import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, L = map(int, rl().split())
    x = set(map(int, rl().split()))
    T1, T2, T3 = map(int, rl().split())
    
    INF = 10 ** 18
    dp = [[INF] * 2 for _ in range(100010)]
    dp[0][0] = 0
    
    for i in range(L):
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + (T1 // 2) + (T2 // 2))
        dp[i + 2][1] = min(dp[i + 2][1], dp[i][0] + (T1 // 2) + (T2 + (T2 // 2)))
        dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + (T1 // 2) + (2 * T2 + (T2 // 2)))
        if i + 1 in x:
            dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + T1 + T3)
        else:
            dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + T1)
        if i + 2 in x:
            dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + T1 + T2 + T3)
        else:
            dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + T1 + T2)
        if i + 4 in x:
            dp[i + 4][0] = min(dp[i + 4][0], dp[i][0] + T1 + 3 * T2 + T3)
        else:
            dp[i + 4][0] = min(dp[i + 4][0], dp[i][0] + T1 + 3 * T2)
    print(min(dp[L]))


if __name__ == '__main__':
    solve()
