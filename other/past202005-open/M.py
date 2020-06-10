import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(lambda n: int(n) - 1, rl().split())
        graph[u].append(v)
        graph[v].append(u)
    s = int(rl()) - 1
    K = int(rl())
    t = list(map(lambda n: int(n) - 1, rl().split()))
    
    INF = 10 ** 9
    costs = [[INF] * N for _ in range(K + 1)]
    for i, s_node in enumerate([s] + t):
        costs[i][s_node] = 0
        que = deque([s_node])
        while que:
            cur = que.popleft()
            for child in graph[cur]:
                if costs[i][child] == INF:
                    costs[i][child] = costs[i][cur] + 1
                    que.append(child)
    
    dp = [[INF] * (K + 1) for _ in range(1 << (K + 1))]
    dp[1][0] = 0
    for S in range(1, 1 << (K + 1)):
        if not S & 1:
            continue
        target = []
        for j in range(1, K + 1):
            if not S >> j & 1:
                target.append(j)
        for j in range(K + 1):
            for k in target:
                dp[S | (1 << k)][k] = min(dp[S | (1 << k)][k], dp[S][j] + costs[j][t[k - 1]])
    print(min(dp[(1 << (K + 1)) - 1]))


if __name__ == '__main__':
    solve()
