import sys
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class SegmentTree:
    def __init__(self, init_value: list, segfunc, ide_ele):
        n = len(init_value)
        self.N0 = 1 << (n - 1).bit_length()
        self.ide_ele = ide_ele
        self.data = [ide_ele] * (2 * self.N0)
        self.segfunc = segfunc
        
        for i, x in enumerate(init_value):
            self.data[i + self.N0 - 1] = x
        for i in range(self.N0 - 2, -1, -1):
            self.data[i] = self.segfunc(self.data[2 * i + 1], self.data[2 * i + 2])
    
    def update(self, k, x):
        k += self.N0 - 1
        ################################################################
        self.data[k] = x
        ################################################################
        while k:
            k = (k - 1) // 2
            self.data[k] = self.segfunc(self.data[k * 2 + 1], self.data[k * 2 + 2])
    
    def query(self, left, right):
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
        ################################################################
        
        while L < R:
            if L & 1:
                res = self.segfunc(res, self.data[L - 1])
                L += 1
            if R & 1:
                R -= 1
                res = self.segfunc(res, self.data[R - 1])
            L >>= 1
            R >>= 1
        
        ################################################################
        return res


def solve():
    N, M = map(int, rl().split())
    LRC = [list(map(int, rl().split())) for _ in range(M)]
    LRC.sort(key=itemgetter(0, 1))
    
    INF = 10 ** 18
    dist = [INF] * N
    dist[0] = 0
    seg_tree = SegmentTree(dist, min, INF)
    
    for L, R, C in LRC:
        L, R = L - 1, R - 1
        tmp = seg_tree.query(L, R)
        cost = tmp + C
        if cost < dist[R]:
            dist[R] = cost
            seg_tree.update(R, cost)
    print(dist[-1] if dist[-1] != INF else -1)


if __name__ == '__main__':
    solve()
