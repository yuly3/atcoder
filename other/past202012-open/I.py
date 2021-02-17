import sys
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, K = map(int, rl().split())
    H = list(map(int, rl().split()))
    C = list(map(lambda n: int(n) - 1, rl().split()))
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda n: int(n) - 1, rl().split())
        if H[a] < H[b]:
            graph[b].append(a)
        else:
            graph[a].append(b)
    
    INF = 10 ** 9
    dist = [INF] * N
    for ci in C:
        dist[ci] = 0
    
    H = [(hi, i) for i, hi in enumerate(H)]
    H.sort(key=itemgetter(0))
    ans = [-1] * N
    for _, i in H:
        for to in graph[i]:
            dist[i] = min(dist[i], dist[to] + 1)
        if dist[i] != INF:
            ans[i] = dist[i]
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
