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


def solve():
    N, Q = map(int, rl().split())
    C = list(map(int, rl().split()))
    
    uf = UnionFind(N)
    dict_list = [defaultdict(int) for _ in range(N)]
    for i, ci in enumerate(C):
        dict_list[i][ci] = 1
    
    ans = []
    for _ in range(Q):
        com, *q = map(int, rl().split())
        if com == 1:
            a, b = map(lambda n: n - 1, q)
            root0 = uf.find(a)
            root1 = uf.find(b)
            if uf.same(root0, root1):
                continue
            if uf.size(root0) < uf.size(root1):
                root0, root1 = root1, root0
            for key, val in dict_list[root1].items():
                dict_list[root0][key] += val
            uf.union(a, b)
        else:
            x, y = q
            x -= 1
            ans.append(dict_list[uf.find(x)][y])
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
