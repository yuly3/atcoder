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
    N = int(rl())
    A = list(map(int, rl().split()))
    B = list(map(int, rl().split()))
    
    A = [(ai, i) for i, ai in enumerate(A)]
    A.sort(key=itemgetter(0))
    B.sort()
    init_val = [0] * (N + 1)
    for i in range(N):
        init_val[i] = max(A[i][0] - B[i], 0)
    seg_tree = SegmentTree(init_val, max, 0)
    
    ans = [0] * (N + 1)
    ans[A[-1][1]] = seg_tree.data[0]
    
    for i in range(N - 1, -1, -1):
        seg_tree.update(i, 0)
        seg_tree.update(i + 1, max(A[i + 1][0] - B[i], 0))
        ans[A[i][1]] = seg_tree.data[0]
    print(*ans)


if __name__ == '__main__':
    solve()
