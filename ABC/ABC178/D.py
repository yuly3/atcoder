import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 10 ** 9 + 7
    S = int(rl())
    
    dp = [[0] * (S + 1) for _ in range(S + 1)]
    dp[0][0] = 1
    
    for i in range(S):
        for j in range(2, S):
            dp[i + 1][j + 1] = (dp[i + 1][j] + dp[i][j - 2]) % MOD
    
    ans = 0
    for i in range(1, (S // 3) + 1):
        ans += dp[i][S]
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
