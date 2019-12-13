import numpy as np


def solve():
    N, T = map(int, input().split())
    ab_l = [[0, 0] for _ in range(N)]
    for i in range(N):
        ab_l[i][0], ab_l[i][1] = map(int, input().split())
    ab_l.sort()
    dp = np.zeros(T, dtype=int)
    ans = 0

    for a, b in ab_l:
        ans = max(ans, dp[-1] + b)
        dp[a:] = np.maximum(dp[a:], dp[:-a]+b)

    print(ans)


if __name__ == '__main__':
    solve()