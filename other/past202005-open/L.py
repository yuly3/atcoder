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
    _ = rl()
    a = tuple(map(int, rl().split()))
    
    ide_ele = (0, -1)
    init_arr0, init_arr1 = [], []
    for i in range(N):
        tij = T[i].popleft()
        init_arr0.append((tij, i))
        if T[i]:
            tij = T[i].popleft()
            init_arr1.append((tij, i))
        else:
            init_arr1.append(ide_ele)
    
    f = lambda A, B: A if B[0] < A[0] else B
    seg_tree0 = SegmentTree(init_arr0, f, ide_ele)
    seg_tree1 = SegmentTree(init_arr1, f, ide_ele)
    
    ans = []
    for ai in a:
        if ai == 1:
            v, idx = seg_tree0.data[0]
            ans.append(v)
            vv = seg_tree1.data[idx + seg_tree1.N0 - 1][0]
            seg_tree0.update(idx, (vv, idx))
            if T[idx]:
                seg_tree1.update(idx, (T[idx].popleft(), idx))
            else:
                seg_tree1.update(idx, ide_ele)
        else:
            v0, idx0 = seg_tree0.data[0]
            v1, idx1 = seg_tree1.data[0]
            if v1 < v0:
                ans.append(v0)
                vv = seg_tree1.data[idx0 + seg_tree1.N0 - 1][0]
                seg_tree0.update(idx0, (vv, idx0))
                if T[idx0]:
                    seg_tree1.update(idx0, (T[idx0].popleft(), idx0))
                else:
                    seg_tree1.update(idx0, ide_ele)
            else:
                ans.append(v1)
                if T[idx1]:
                    seg_tree1.update(idx1, (T[idx1].popleft(), idx1))
                else:
                    seg_tree1.update(idx1, ide_ele)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
