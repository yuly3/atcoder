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
    N, K = map(int, rl().split())
    P = list(map(lambda n: int(n) - 1, rl().split()))
    C = list(map(int, rl().split()))
    
    uf = UnionFind(N)
    for i in range(N):
        uf.union(i, P[i])
    roop_scores = defaultdict(int)
    for i in range(N):
        roop_scores[uf.find(i)] += C[i]
    
    ans = -(10 ** 18)
    K -= 1
    for s in range(N):
        cur = P[s]
        tmp = C[cur]
        ans = max(ans, tmp)
        roop_size = uf.size(s)
        roop_score = roop_scores[uf.find(s)]
        roop_cnt = K // roop_size
        if roop_cnt and 0 < roop_score:
            tmp += roop_score * roop_cnt
            rem = K % roop_size
            ans = max(ans, tmp)
            while rem:
                cur = P[cur]
                tmp += C[cur]
                ans = max(ans, tmp)
                rem -= 1
            continue
        cnt = min(roop_size, K)
        while cnt:
            cur = P[cur]
            tmp += C[cur]
            ans = max(ans, tmp)
            cnt -= 1
    print(ans)


if __name__ == '__main__':
    solve()
