import sys

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
    a = list(map(int, rl().split()))
    
    b = [0] * (N + 1)
    for i, x in enumerate(a):
        b[x] = i
    
    uf = UnionFind(N)
    ans = 0
    for idx in b[:0:-1]:
        left, right = 1, 1
        if 0 <= idx - 1 and a[idx] < a[idx - 1]:
            left += uf.size(idx - 1)
            uf.union(idx - 1, idx)
        if idx + 1 <= N - 1 and a[idx] < a[idx + 1]:
            right += uf.size(idx + 1)
            uf.union(idx, idx + 1)
        ans += left * right * a[idx]
    print(ans)


if __name__ == '__main__':
    solve()
