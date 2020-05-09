import sys
from itertools import combinations
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x: int):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x: int):
        return -self.parents[self.find(x)]
    
    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)
    
    def members(self, x: int):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def solve():
    N, M = map(int, rl().split())
    x, y, c = [0] * N, [0] * N, [0] * N
    for i in range(N):
        x[i], y[i], c[i] = map(int, rl().split())
    X, Y, C = [0] * M, [0] * M, [0] * M
    for i in range(M):
        X[i], Y[i], C[i] = map(int, rl().split())
    
    big_tower_edges = []
    for i, j in combinations(range(N), 2):
        cost = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
        if c[i] != c[j]:
            cost *= 10
        big_tower_edges.append((cost, i, j))
    
    ans = 10 ** 18
    for s in range(1 << M):
        small_towers = []
        for i in range(M):
            if s >> i & 1:
                small_towers.append(i)
        add_edges = []
        for i in small_towers:
            for j in range(N):
                cost = ((X[i] - x[j]) ** 2 + (Y[i] - y[j]) ** 2) ** 0.5
                if C[i] != c[j]:
                    cost *= 10
                add_edges.append((cost, i + N, j))
        for i, j in combinations(small_towers, 2):
            cost = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) ** 0.5
            if C[i] != C[j]:
                cost *= 10
            add_edges.append((cost, i + N, j + N))
        current_edges = big_tower_edges + add_edges
        current_edges.sort(key=itemgetter(0))
        
        uf = UnionFind(N + M)
        tmp = 0
        for cost, i, j in current_edges:
            if not uf.same(i, j):
                tmp += cost
                uf.union(i, j)
        ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    solve()
