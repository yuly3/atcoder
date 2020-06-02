import sys
from collections import defaultdict

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
    x, y = [0] * N, [0] * N
    for i in range(N):
        x[i], y[i] = map(int, rl().split())
    MAX_N = 10 ** 5
    
    uf = UnionFind(2 * MAX_N + 1)
    for xi, yi in zip(x, y):
        uf.union(xi, MAX_N + yi)
    
    x_counter = defaultdict(int)
    y_counter = defaultdict(int)
    for xi in range(1, MAX_N + 1):
        if uf.parents[xi] == -1:
            continue
        x_counter[uf.find(xi)] += 1
    for yi in range(MAX_N + 1, 2 * MAX_N + 1):
        if uf.parents[yi] == -1:
            continue
        y_counter[uf.find(yi)] += 1
    
    united = defaultdict(int)
    for xi in x:
        united[uf.find(xi)] += 1
    
    ans = 0
    for key, val in united.items():
        ans += x_counter[key] * y_counter[key] - val
    print(ans)


if __name__ == '__main__':
    solve()
