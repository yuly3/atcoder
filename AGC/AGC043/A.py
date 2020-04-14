import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    s = [list(input()) for _ in range(H)]
    
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = s[0][0] == '#'
    for i in range(1, W):
        dp[0][i] = dp[0][i - 1] + (s[0][i - 1] == '.' and s[0][i] == '#')
    for i in range(1, H):
        dp[i][0] = dp[i - 1][0] + (s[i - 1][0] == '.' and s[i][0] == '#')
    
    for i in range(1, H):
        for j in range(1, W):
            dy = s[i - 1][j] == '.' and s[i][j] == '#'
            dx = s[i][j - 1] == '.' and s[i][j] == '#'
            dp[i][j] = min(dp[i - 1][j] + dy, dp[i][j - 1] + dx)
    print(dp[-1][-1])


if __name__ == '__main__':
    solve()
