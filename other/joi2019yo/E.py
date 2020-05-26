import sys
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    A = tuple(map(int, rl().split()))
    LR = [tuple(map(int, rl().split())) for _ in range(M)]
    
    LR.sort(key=itemgetter(0))
    left = [-1] * N
    p = -1
    for L, R in LR:
        L, R = L - 1, R - 1
        if R <= p:
            continue
        for i in range(max(p + 1, L), R + 1):
            left[i] = L
        p = R
    
    dp = [0] * (N + 1)
    for i in range(N):
        if left[i] == -1:
            dp[i + 1] = dp[i] + A[i]
        else:
            dp[i + 1] = max(dp[i], dp[left[i]] + A[i])
    print(dp[N])


if __name__ == '__main__':
    solve()
