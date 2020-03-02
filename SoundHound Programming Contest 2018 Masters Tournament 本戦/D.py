from collections import deque


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
    N, Q = map(int, input().split())
    graph = [set() for _ in range(N)]
    connect = [set() for _ in range(N)]
    uf_tree = UnionFind(N)
    
    for _ in range(Q):
        cmd, u, v = map(int, input().split())
        
        if cmd == 1:
            u, v = u - 1, v - 1
            graph[u].add(v)
            graph[v].add(u)
            x, y = uf_tree.find(u), uf_tree.find(v)
            connect[x].add(y)
            connect[y].add(x)
        elif cmd == 2:
            u -= 1
            root = uf_tree.find(u)
            searched = set()
            que = deque([root])
            while que:
                parent = que.pop()
                if parent in searched:
                    continue
                searched.add(parent)
                for child in connect[parent]:
                    if child in searched:
                        continue
                    que.append(child)
                uf_tree.union(root, parent)
                connect[parent].clear()
        else:
            u, v = u - 1, v - 1
            if v in graph[u] or uf_tree.same(u, v):
                print('Yes')
            else:
                print('No')


if __name__ == '__main__':
    solve()
