import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    dp = [0] * N
    dp[1] = max(A[:2])
    odd = A[0]
    
    for i in range(2, N):
        if i % 2 == 0:
            odd += A[i]
            dp[i] = max(dp[i - 2] + A[i], dp[i - 1])
        else:
            dp[i] = max(dp[i - 2] + A[i], odd)
    print(dp[-1])


if __name__ == '__main__':
    solve()
