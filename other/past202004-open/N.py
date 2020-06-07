import sys
from operator import itemgetter, add

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class DualSegmentTree:
    def __init__(self, init_value: list, segfunc, lazy_ide_ele=0):
        self.lazy_ide_ele = lazy_ide_ele
        self.segfunc = segfunc
        n = len(init_value)
        self.N0 = 1 << (n - 1).bit_length()
        self.lazy = [self.lazy_ide_ele] * (2 * self.N0)
    
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
            self.lazy[2 * idx + 1] = self.segfunc(self.lazy[2 * idx + 1], v)
            self.lazy[2 * idx + 2] = self.segfunc(self.lazy[2 * idx + 2], v)
            self.lazy[idx] = self.lazy_ide_ele
    
    def update(self, left, right, x):
        ids = tuple(self.gindex(left, right))
        self.propagates(*ids)
        L = self.N0 + left
        R = self.N0 + right
        
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] = self.segfunc(self.lazy[R - 1], x)
            if L & 1:
                self.lazy[L - 1] = self.segfunc(self.lazy[L - 1], x)
                L += 1
            L >>= 1
            R >>= 1
    
    def query(self, k):
        self.propagates(*self.gindex(k, k + 1))
        return self.lazy[k + self.N0 - 1]


def solve():
    N, Q = map(int, rl().split())
    xmin, ymin, D, C = [0] * N, [0] * N, [0] * N, [0] * N
    for i in range(N):
        xmin[i], ymin[i], D[i], C[i] = map(int, rl().split())
    A, B = [0] * Q, [0] * Q
    for i in range(Q):
        A[i], B[i] = map(int, rl().split())
    
    events = []
    y = set()
    for i in range(N):
        events.append((0, xmin[i], ymin[i], ymin[i] + D[i], C[i]))
        events.append((2, xmin[i] + D[i], ymin[i], ymin[i] + D[i], C[i]))
        y.add(ymin[i])
        y.add(ymin[i] + D[i])
    for i in range(Q):
        events.append((1, A[i], B[i], i))
        y.add(B[i])
    
    events.sort(key=itemgetter(1, 0))
    y_to_idx = {val: idx for idx, val in enumerate(sorted(y))}
    
    dual_seg_tree = DualSegmentTree([0] * len(y), add)
    ans = [0] * Q
    for com, *event in events:
        if com == 0:
            _, ys, ye, cost = event
            dual_seg_tree.update(y_to_idx[ys], y_to_idx[ye] + 1, cost)
        elif com == 2:
            _, ys, ye, cost = event
            dual_seg_tree.update(y_to_idx[ys], y_to_idx[ye] + 1, -cost)
        else:
            _, bi, qi = event
            ans[qi] = dual_seg_tree.query(y_to_idx[bi])
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
