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


def sovle():
    N, M = map(int, input().split())
    uf_tree = UnionFind(N)
    closed_circit_node = set()
    for _ in range(M):
        u, v = map(lambda x: int(x) - 1, input().split())
        if uf_tree.same(u, v):
            closed_circit_node.add(u)
            closed_circit_node.add(v)
        else:
            uf_tree.union(u, v)
    
    closed_circit_root = set()
    for node in closed_circit_node:
        closed_circit_root.add(uf_tree.find(node))
    
    ans = uf_tree.group_count() - len(closed_circit_root)
    print(ans)


if __name__ == '__main__':
    sovle()
