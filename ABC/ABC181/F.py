import sys
from itertools import combinations
from math import hypot
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
    N = int(rl())
    xy = [list(map(int, rl().split())) for _ in range(N)]
    
    edges = []
    s, t = N, N + 1
    for i, (_, yi) in enumerate(xy):
        edges.append((100 - yi, i, s))
        edges.append((yi + 100, i, t))
    for i, j in combinations(range(N), 2):
        xi, yi = xy[i]
        xj, yj = xy[j]
        edges.append((hypot(xi - xj, yi - yj), i, j))
    edges.sort(key=itemgetter(0))
    
    uf = UnionFind(N + 2)
    for dist, u, v in edges:
        uf.union(u, v)
        if uf.same(s, t):
            print(dist / 2)
            return


if __name__ == '__main__':
    solve()
