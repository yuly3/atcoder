import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    graph = [0] * N
    for _ in range(M):
        a, b = map(lambda n: int(n) - 1, rl().split())
        graph[a] |= 1 << b
        graph[b] |= 1 << a
    
    dp = [0xff] * (1 << N)
    dp[0] = 1
    for i in range(N):
        for j in range(1 << N):
            if dp[j] == 1 and (graph[i] & j) == j:
                dp[j | 1 << i] = 1
    
    for i in range(1 << N):
        j = i
        while j:
            dp[i] = min(dp[i], dp[j] + dp[i ^ j])
            j -= 1
            j &= i
    print(dp[-1])


if __name__ == '__main__':
    solve()
