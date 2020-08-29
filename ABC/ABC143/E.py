import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, L = map(int, rl().split())
    INF = 10 ** 18
    dist = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, rl().split())
        a, b = a - 1, b - 1
        dist[a][b] = dist[b][a] = c
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    cost = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dist[i][j] <= L:
                cost[i][j] = 1
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    
    Q = int(rl())
    st = [list(map(lambda n: int(n) - 1, rl().split())) for _ in range(Q)]
    ans = [-1] * Q
    for i, (s, t) in enumerate(st):
        if cost[s][t] != INF:
            ans[i] = cost[s][t] - 1
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
