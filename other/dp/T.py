import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    s = input()
    MOD = 10 ** 9 + 7
    
    dp = [[0] * N for _ in range(N)]
    acc = [i for i in range(1, N + 1)]
    
    for i in range(1, N):
        for j in range(N - i + 1):
            if s[i - 1] == '<':
                dp[i][j] = (acc[N - i] - acc[j]) % MOD
            else:
                dp[i][j] = acc[j]
        acc[0] = dp[i][0]
        for j in range(1, N):
            acc[j] = (acc[j - 1] + dp[i][j]) % MOD
    print(dp[-1][0])


if __name__ == '__main__':
    solve()
