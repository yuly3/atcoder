from operator import itemgetter


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
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
    N = int(input())
    xy = [list(map(lambda x: int(x) - 1, input().split())) + [i] for i in range(N)]
    
    sorted_x = sorted(xy, key=itemgetter(0, 1))
    sorted_y = sorted(xy, key=itemgetter(1, 0))
    edges = []
    for i in range(N - 1):
        cost = min(abs(sorted_x[i][0] - sorted_x[i + 1][0]), abs(sorted_x[i][1] - sorted_x[i + 1][1]))
        edges.append([cost, sorted_x[i][2], sorted_x[i + 1][2]])
        cost = min(abs(sorted_y[i][0] - sorted_y[i + 1][0]), abs(sorted_y[i][1] - sorted_y[i + 1][1]))
        edges.append([cost, sorted_y[i][2], sorted_y[i + 1][2]])
    edges.sort(key=itemgetter(0))
    
    ans = 0
    uf_tree = UnionFind(N)
    for cost, u, v in edges:
        if not uf_tree.same(u, v):
            ans += cost
            uf_tree.union(u, v)
    print(ans)


if __name__ == '__main__':
    solve()
