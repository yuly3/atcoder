import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = None
        self.it = None
    
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.graph[fr].append(forward)
        self.graph[to].append(backward)
    
    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.graph[v1].append(edge1)
        self.graph[v2].append(edge2)
    
    def bfs(self, s, t):
        self.level = level = [-1] * self.n
        deq = deque([s])
        level[s] = 0
        G = self.graph
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] == -1:
                    level[w] = lv
                    deq.append(w)
        return level[t] != -1
    
    def dfs(self, v, t, f):
        if v == t:
            return f
        for e in self.it[v]:
            w, cap, rev = e
            if cap and self.level[v] < self.level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
    
    def flow(self, s, t):
        flow = 0
        INF = 10 ** 18
        while self.bfs(s, t):
            *self.it, = map(iter, self.graph)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


def solve():
    N, G, E = map(int, rl().split())
    dinic = Dinic(N + 1)
    p = list(map(int, rl().split()))
    for pi in p:
        dinic.add_edge(pi, N, 1)
    for _ in range(E):
        a, b = map(int, rl().split())
        dinic.add_multi_edge(a, b, 1, 1)
    
    ans = dinic.flow(0, N)
    print(ans)


if __name__ == '__main__':
    solve()
