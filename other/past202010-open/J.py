import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    X = list(map(int, rl().split()))
    X = ((0, X[0], X[1]),
         (X[0], 0, X[2]),
         (X[1], X[2], 0))
    S = rl().rstrip()
    graph = [[] for _ in range(N + 3)]
    for _ in range(M):
        a, b, c = map(int, rl().split())
        a, b = a - 1, b - 1
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    S = [ord(si) - ord('A') for si in S]
    S_set = set(S)
    for i, si in enumerate(S):
        for j in range(3):
            if si == j:
                graph[N + j].append((i, 0))
                continue
            if j not in S_set:
                continue
            graph[i].append((N + j, X[si][j]))
    
    min_dist = [10 ** 18] * (N + 3)
    que = [(0, 0)]
    while que:
        t, cur = heappop(que)
        if cur == N - 1:
            print(t)
            break
        if min_dist[cur] < t:
            continue
        for to, cost in graph[cur]:
            nt = t + cost
            if min_dist[to] <= nt:
                continue
            min_dist[to] = nt
            heappush(que, (nt, to))


if __name__ == '__main__':
    solve()
