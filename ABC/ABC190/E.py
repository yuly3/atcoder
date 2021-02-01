import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        ai, bi = map(lambda n: int(n) - 1, rl().split())
        graph[ai].append(bi)
        graph[bi].append(ai)
    K = int(rl())
    C = list(map(lambda n: int(n) - 1, rl().split()))
    
    c_set = set(C)
    c_to_idx = {ci: i for i, ci in enumerate(C)}
    INF = 10 ** 18
    dist = [[INF] * K for _ in range(K)]
    for i in range(K):
        que = deque([(-1, C[i], 0)])
        searched = [False] * N
        searched[C[i]] = True
        while que:
            parent, cur, d = que.popleft()
            for child in graph[cur]:
                if child == parent or searched[child]:
                    continue
                if child in c_set:
                    dist[i][c_to_idx[child]] = d + 1
                searched[child] = True
                que.append((cur, child, d + 1))
    
    dp = [[INF] * K for _ in range(2 ** K)]
    for i in range(K):
        dp[1 << i][i] = 0
    
    for s in range(1, 2 ** K):
        for i in range(K):
            if s >> i & 1:
                continue
            ns = s | (1 << i)
            for j in range(K):
                if i == j:
                    continue
                dp[ns][i] = min(dp[ns][i], dp[s][j] + dist[j][i])
    
    ans = min(dp[2 ** K - 1])
    if ans == INF:
        print(-1)
    else:
        print(ans + 1)


if __name__ == '__main__':
    solve()
