import sys
from operator import add, itemgetter

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
    
    def update(self, k: int, x):
        k += self.N0 - 1
        ################################################################
        self.data[k] = x
        ################################################################
        while k:
            k = (k - 1) // 2
            self.data[k] = self.segfunc(self.data[k * 2 + 1], self.data[k * 2 + 2])
    
    def query(self, left: int, right: int):
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
    N, Q = map(int, rl().split())
    c = list(map(lambda n: int(n) - 1, rl().split()))
    lr = [list(map(int, rl().split())) for _ in range(Q)]
    
    query = sorted([(left - 1, right, idx) for idx, (left, right) in enumerate(lr)], key=itemgetter(1))
    seg_tree = SegmentTree([0] * N, add, 0)
    c_to_idx = [-1] * N
    
    p_right = 0
    ans = [0] * Q
    for left, right, idx in query:
        for i in range(p_right, right):
            if c_to_idx[c[i]] != -1:
                seg_tree.update(c_to_idx[c[i]], 0)
            seg_tree.update(i, 1)
            c_to_idx[c[i]] = i
        p_right = right
        ans[idx] = seg_tree.query(left, right)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
