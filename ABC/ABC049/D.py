from collections import defaultdict


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
    N, K, L = map(int, input().split())
    connect_road, connect_rail = UnionFind(N), UnionFind(N)
    for _ in range(K):
        p, q = map(lambda x: int(x) - 1, input().split())
        connect_road.union(p, q)
    for _ in range(L):
        r, s = map(lambda x: int(x) - 1, input().split())
        connect_rail.union(r, s)
    
    root = defaultdict(int)
    for i in range(N):
        root[(connect_road.find(i), connect_rail.find(i))] += 1
    for i in range(N):
        print(root[(connect_road.find(i), connect_rail.find(i))])


if __name__ == '__main__':
    solve()
