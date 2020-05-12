import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = tuple(int(rl()) for _ in range(N)) * 2
    
    dp = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
    ans = 0
    for i in range(N):
        for left in range(2 * N - i):
            right = i + left
            if (N - i) % 2 == 1:
                dp[left][right] = max(dp[left + 1][right] + A[left], dp[left][right - 1] + A[right])
            else:
                if A[left] < A[right]:
                    dp[left][right] = dp[left][right - 1]
                else:
                    dp[left][right] = dp[left + 1][right]
            if i == N - 1:
                ans = max(ans, dp[left][right])
    print(ans)


if __name__ == '__main__':
    solve()
