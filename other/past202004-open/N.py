import sys
from operator import itemgetter, add

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class LazySegmentTree:
    def __init__(self, init_value: list, segfunc, ide_ele=0, lazy_ide_ele=0):
        self.ide_ele = ide_ele
        self.lazy_ide_ele = lazy_ide_ele
        self.segfunc = segfunc
        n = len(init_value)
        self.N0 = 1 << (n - 1).bit_length()
        self.data = [self.ide_ele] * (2 * self.N0)
        self.lazy = [self.lazy_ide_ele] * (2 * self.N0)
        
        for i, x in enumerate(init_value):
            self.data[i + self.N0 - 1] = x
        for i in range(self.N0 - 2, -1, -1):
            self.data[i] = segfunc(self.data[2 * i + 1], self.data[2 * i + 2])
    
    def gindex(self, left, right):
        L = left + self.N0
        R = right + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1
            R >>= 1
        while L:
            yield L
            L >>= 1
    
    def propagates(self, *ids):
        for i in reversed(ids):
            idx = i - 1
            v = self.lazy[idx]
            if v == self.lazy_ide_ele:
                continue
            ################################################################
            self.data[2 * idx + 1] += v
            self.data[2 * idx + 2] += v
            self.lazy[2 * idx + 1] += v
            self.lazy[2 * idx + 2] += v
            ################################################################
            self.lazy[idx] = self.lazy_ide_ele
    
    def update(self, left, right, x):
        ids = tuple(self.gindex(left, right))
        ################################################################
        self.propagates(*ids)
        ################################################################
        L = self.N0 + left
        R = self.N0 + right
        
        while L < R:
            if R & 1:
                R -= 1
                ################################################################
                self.lazy[R - 1] += x
                self.data[R - 1] += x
                ################################################################
            if L & 1:
                ################################################################
                self.lazy[L - 1] += x
                self.data[L - 1] += x
                ################################################################
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            idx = i - 1
            self.data[idx] = self.segfunc(self.data[2 * idx + 1], self.data[2 * idx + 2])
    
    def query(self, left, right):
        self.propagates(*self.gindex(left, right))
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
    xmin, ymin, D, C = [0] * N, [0] * N, [0] * N, [0] * N
    for i in range(N):
        xmin[i], ymin[i], D[i], C[i] = map(int, rl().split())
    A, B = [0] * Q, [0] * Q
    for i in range(Q):
        A[i], B[i] = map(int, rl().split())
    
    events = []
    y = []
    for i in range(N):
        events.append((0, xmin[i], ymin[i], ymin[i] + D[i], C[i]))
        events.append((2, xmin[i] + D[i], ymin[i], ymin[i] + D[i], C[i]))
        y.append(ymin[i])
        y.append(ymin[i] + D[i])
    for i in range(Q):
        events.append((1, A[i], B[i], i))
        y.append(B[i])
    
    events.sort(key=itemgetter(1, 0))
    idx_to_y = sorted(set(y))
    y_to_idx = {val: idx for idx, val in enumerate(idx_to_y)}
    
    M = len(idx_to_y)
    lazy_seg_tree = LazySegmentTree([0] * M, add)
    ans = [0] * Q
    for com, *event in events:
        if com == 0:
            _, ys, ye, cost = event
            lazy_seg_tree.update(y_to_idx[ys], y_to_idx[ye] + 1, cost)
        elif com == 2:
            _, ys, ye, cost = event
            lazy_seg_tree.update(y_to_idx[ys], y_to_idx[ye] + 1, -cost)
        else:
            _, bi, qi = event
            ans[qi] = lazy_seg_tree.query(y_to_idx[bi], y_to_idx[bi] + 1)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
