import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    INF = 10 ** 12
    dist = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, rl().split())
        a, b = a - 1, b - 1
        dist[a][b] = min(dist[a][b], c)
    graph = [[] for _ in range(N)]
    for i, dist_i in enumerate(dist):
        for j, dist_ij in enumerate(dist_i):
            if dist_ij != INF:
                graph[i].append((j, dist_ij))
    
    ans = []
    for s in range(N):
        que = [(0, s)]
        searched = [INF] * N
        while True:
            t, cur = heappop(que)
            if t != 0 and cur == s:
                ans.append(t)
                break
            if searched[cur] < t:
                if not que:
                    ans.append(-1)
                    break
                else:
                    continue
            for child, cost in graph[cur]:
                nt = t + cost
                if searched[child] <= nt:
                    continue
                searched[child] = nt
                heappush(que, (nt, child))
            if not que:
                ans.append(-1)
                break
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    solve()
