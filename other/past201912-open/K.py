import sys
from collections import deque

rl = sys.stdin.readline


class LowestCommonAncestor:
    def __init__(self, tree, root):
        self.n = len(tree)
        self.depth = [0] * self.n
        self.log_size = self.n.bit_length()
        self.parent = [[-1] * self.n for _ in range(self.log_size)]
        
        q = deque([(root, -1, 0)])
        while q:
            v, par, dist = q.pop()
            self.parent[0][v] = par
            self.depth[v] = dist
            for child in tree[v]:
                if child != par:
                    self.depth[child] = dist + 1
                    q.append((child, v, dist + 1))
        
        for k in range(1, self.log_size):
            for v in range(self.n):
                self.parent[k][v] = self.parent[k - 1][self.parent[k - 1][v]]
    
    def lca(self, _u, _v):
        u, v = _u, _v
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        for k in range(self.log_size):
            if self.depth[v] - self.depth[u] >> k & 1:
                v = self.parent[k][v]
        if u == v:
            return u
        
        for k in reversed(range(self.log_size)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][v]


def solve():
    N = int(rl())
    tree = [[] for _ in range(N)]
    root = 0
    for i in range(N):
        pi = int(rl())
        if pi == -1:
            root = i
            continue
        tree[i].append(pi - 1)
        tree[pi - 1].append(i)
    
    doubling = LowestCommonAncestor(tree, root)
    Q = int(rl())
    for _ in range(Q):
        a, b = map(lambda x: int(x) - 1, rl().split())
        if doubling.lca(a, b) == b:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    solve()
