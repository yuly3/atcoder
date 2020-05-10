import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = rl().rstrip()
    C = list(map(int, rl().split()))
    D = list(map(int, rl().split()))
    
    INF = 10 ** 18
    dp = [[INF] * 3000 for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(N):
        if S[i] == ')':
            k = -1
        else:
            k = 1
        for j in range(2999):
            if 0 <= j + k:
                dp[i + 1][j + k] = min(dp[i + 1][j + k], dp[i][j])
            if 0 <= j - k:
                dp[i + 1][j - k] = min(dp[i + 1][j - k], dp[i][j] + C[i])
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + D[i])
    print(dp[N][0])


if __name__ == '__main__':
    solve()
