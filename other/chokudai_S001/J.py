import sys
from operator import add

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
    
    def update(self, _k, x):
        k = _k + self.N0 - 1
        self.data[k] = x
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
    a = list(map(int, rl().split()))
    
    compress = {ai: i for i, ai in enumerate(sorted(a))}
    seg_tree = SegmentTree([0] * N, add, 0)
    
    ans = 0
    for i in range(N - 1, -1, -1):
        num = compress[a[i]]
        ans += seg_tree.query(0, num + 1)
        seg_tree.update(num, 1)
    print(ans)


if __name__ == '__main__':
    solve()
