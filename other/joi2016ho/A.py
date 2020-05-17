import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, K = map(int, rl().split())
    A = [int(rl()) for _ in range(N)]
    
    dp = [10 ** 18] * (N + 1)
    dp[0] = 0
    for i in range(N):
        min_a, max_a = A[i], A[i]
        for j in range(i + 1, min(N + 1, i + M + 1)):
            dp[j] = min(dp[j], dp[i] + K + (j - i) * (max_a - min_a))
            if j < N:
                min_a = min(min_a, A[j])
                max_a = max(max_a, A[j])
    print(dp[N])


if __name__ == '__main__':
    solve()
