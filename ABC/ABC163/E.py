import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    infants = [(ai, i) for i, ai in enumerate(A)]
    infants.sort(reverse=True)
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    ans = 0
    for x in range(N):
        for y in range(N):
            if x + y == N:
                ans = max(ans, dp[x][y])
                break
            act_level, idx = infants[x + y]
            dp[x + 1][y] = max(dp[x + 1][y], dp[x][y] + act_level * abs(idx - x))
            dp[x][y + 1] = max(dp[x][y + 1], dp[x][y] + act_level * abs(idx - (N - y - 1)))
    print(ans)


if __name__ == '__main__':
    solve()
