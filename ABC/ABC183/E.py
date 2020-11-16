import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 10 ** 9 + 7
    H, W = map(int, rl().split())
    S = [rl().rstrip() for _ in range(H)]
    
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[1][1] = 1
    
    acc0 = [[0] * (W + 1) for _ in range(H + 1)]
    acc1 = [[0] * (W + 1) for _ in range(H + 1)]
    acc2 = [[0] * (W + 1) for _ in range(H + 1)]
    
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if S[i - 1][j - 1] == '#':
                dp[i][j] = acc0[i][j] = acc1[i][j] = acc2[i][j] = 0
                continue
            dp[i][j] = (dp[i][j] + acc0[i - 1][j] + acc1[i][j - 1] + acc2[i - 1][j - 1]) % MOD
            acc0[i][j] = (dp[i][j] + acc0[i - 1][j]) % MOD
            acc1[i][j] = (dp[i][j] + acc1[i][j - 1]) % MOD
            acc2[i][j] = (dp[i][j] + acc2[i - 1][j - 1]) % MOD
    print(dp[-1][-1])


if __name__ == '__main__':
    solve()
