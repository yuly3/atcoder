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
    N, M, K = map(int, input().split())
    uf_tree = UnionFind(N + 1)
    ans = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        uf_tree.union(a, b)
        ans[a] -= 1
        ans[b] -= 1
    for _ in range(K):
        c, d = map(int, input().split())
        if uf_tree.same(c, d):
            ans[c] -= 1
            ans[d] -= 1
    
    for i in range(1, N + 1):
        ans[i] += uf_tree.size(i) - 1
    
    print(' '.join(map(str, ans[1:])))


if __name__ == '__main__':
    solve()
