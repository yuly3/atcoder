import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 10 ** 9 + 7
    S = rl().rstrip()
    
    N = len(S)
    dp = [[0 for _ in range(13)] for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(N):
        if S[i] == '?':
            for j in range(10):
                for k in range(13):
                    dp[i + 1][(k * 10 + j) % 13] += dp[i][k] % MOD
        else:
            num = int(S[i])
            for j in range(13):
                dp[i + 1][(j * 10 + num) % 13] += dp[i][j] % MOD
    print(dp[N][5] % MOD)


if __name__ == '__main__':
    solve()
