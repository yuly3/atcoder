import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 10 ** 9 + 7
    N, K = rl().split()
    K = int(K)
    
    hex_to_num = {si: i for i, si in enumerate('0123456789ABCDEF')}
    M = len(N)
    dp = [[0] * 17 for _ in range(M + 1)]
    dp[1][1] = hex_to_num[N[0]] - 1
    S = {hex_to_num[N[0]]}
    
    for i in range(2, M + 1):
        h = hex_to_num[N[i - 1]]
        dp[i][1] += 15
        for j in range(1, 17):
            dp[i][j] += dp[i - 1][j] * j
            dp[i][j] += dp[i - 1][j - 1] * (17 - j)
            if len(S) == j:
                for k in S:
                    dp[i][j] += k < h
            elif len(S) == j - 1:
                for k in range(h):
                    dp[i][j] += k not in S
            dp[i][j] %= MOD
        S.add(h)
    
    ans = dp[M][K]
    ans += len(S) == K
    print(ans)


if __name__ == '__main__':
    solve()
