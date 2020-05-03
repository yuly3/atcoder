import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    INF = 10 ** 18
    N = int(rl())
    A = list(map(int, rl().split()))
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(lambda x: int(x) - 1, rl().split())
        graph[u].append(v)
        graph[v].append(u)
    
    ans = [-1] * N
    stack = [0]
    dp = [INF] * (N + 1)
    rewind = [(-1, -1) for _ in range(N)]
    while stack:
        node = stack.pop()
        if 0 <= node:
            idx = bisect_left(dp, A[node])
            rewind[node] = (idx, dp[idx])
            dp[idx] = A[node]
            ans[node] = bisect_left(dp, INF)
            stack.append(~node)
            for child in graph[node]:
                if ans[child] == -1:
                    stack.append(child)
        else:
            idx, val = rewind[~node]
            dp[idx] = val
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
