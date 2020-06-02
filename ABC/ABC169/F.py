import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 998244353
    N, S = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    dp = [[0] * 3010 for _ in range(3010)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S + 1):
            dp[i + 1][j] += 2 * dp[i][j]
            dp[i + 1][j] %= MOD
            if j + A[i] <= S:
                dp[i + 1][j + A[i]] += dp[i][j]
                dp[i + 1][j + A[i]] %= MOD
    print(dp[N][S])


if __name__ == '__main__':
    solve()
