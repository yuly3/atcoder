import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline
INF = 10 ** 18


def reachable_nodes(s, edges):
    cur = {s}
    reachable = set()
    while cur:
        reachable |= cur
        cur = set().union(*(edges[node] for node in cur)) - reachable
    return reachable


def bellman_ford(n, edges, s):
    dists = [INF] * n
    dists[s] = 0
    for cnt in range(n):
        for u, v, cost in edges:
            if dists[u] != INF and dists[u] + cost < dists[v]:
                if cnt == n - 1:
                    return -1
                dists[v] = dists[u] + cost
    return dists


def solve():
    N, M, P = map(int, rl().split())
    A, B, C = [0] * M, [0] * M, [0] * M
    to = [[] for _ in range(N)]
    reverse_to = [[] for _ in range(N)]
    for i in range(M):
        a, b, c = map(int, rl().split())
        a, b = a - 1, b - 1
        A[i], B[i], C[i] = a, b, P - c
        to[a].append(b)
        reverse_to[b].append(a)
    
    reachable = reachable_nodes(0, to) & reachable_nodes(N - 1, reverse_to)
    
    edge_dict = dict()
    for a, b, c in zip(A, B, C):
        if a in reachable and b in reachable:
            edge_dict[(a, b)] = min(c, edge_dict.get((a, b), 10 ** 6))
    edges = [(u, v, cost) for (u, v), cost in edge_dict.items()]
    
    dists = bellman_ford(N, edges, 0)
    if dists == -1:
        print(-1)
    else:
        print(max(0, -dists[-1]))


if __name__ == '__main__':
    solve()
