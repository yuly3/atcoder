import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = [rl().rstrip() for _ in range(N)]
    
    dp = [[0, 0] for _ in range(N + 1)]
    dp[0] = [1, 1]
    
    for i in range(N):
        for j in range(2):
            for pj in range(2):
                if S[i] == 'AND':
                    dp[i + 1][j & pj] += dp[i][pj]
                else:
                    dp[i + 1][j | pj] += dp[i][pj]
    print(dp[N][1])


if __name__ == '__main__':
    solve()
