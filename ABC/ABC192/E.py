import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, X, Y = map(int, rl().split())
    X, Y = X - 1, Y - 1
    graph = [[] for _ in range(N)]
    T, K = [0] * M, [0] * M
    for i in range(M):
        a, b, t, k = map(int, rl().split())
        a, b = a - 1, b - 1
        graph[a].append((b, i))
        graph[b].append((a, i))
        T[i] = t
        K[i] = k
    
    dist = [10 ** 18] * N
    dist[X] = 0
    que = [(0, X)]
    while que:
        time, cur = heappop(que)
        if cur == Y:
            print(time)
            return
        if dist[cur] < time:
            continue
        for to, idx in graph[cur]:
            wait = K[idx] * (time // K[idx] + 1) - time
            if wait == K[idx]:
                wait = 0
            next_t = time + wait + T[idx]
            if dist[to] <= next_t:
                continue
            dist[to] = next_t
            heappush(que, (next_t, to))
    print(-1)


if __name__ == '__main__':
    solve()
