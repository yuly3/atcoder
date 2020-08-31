import sys
from collections import deque

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
    N = int(rl())
    T = []
    for _ in range(N):
        _, *ti = map(int, rl().split())
        T.append(deque(ti))
    M = int(rl())
    a = tuple(map(int, rl().split()))
    
    ide_ele = (0, -1)
    init_arr0, init_arr1 = [], []
    for i in range(N):
        init_arr0.append((T[i].popleft(), i))
        init_arr1.append((T[i].popleft() if T[i] else 0, i))
    
    f = lambda A, B: A if B[0] < A[0] else B
    seg_tree0 = SegmentTree(init_arr0, f, ide_ele)
    seg_tree1 = SegmentTree(init_arr1, f, ide_ele)
    
    ans = [0] * M
    for i, ai in enumerate(a):
        if ai == 1 or seg_tree1.data[0][0] < seg_tree0.data[0][0]:
            ans[i], idx = seg_tree0.data[0]
            seg_tree0.update(idx, seg_tree1.data[idx + seg_tree1.N0 - 1])
            seg_tree1.update(idx, (T[idx].popleft() if T[idx] else 0, idx))
        else:
            ans[i], idx = seg_tree1.data[0]
            seg_tree1.update(idx, (T[idx].popleft() if T[idx] else 0, idx))
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
