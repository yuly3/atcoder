import sys

rl = sys.stdin.readline


class LazySegmentTree:
    def __init__(self, ls: list, segfunc, identity_element=0, lazy_ide=0):
        self.ide_ele = identity_element
        self.lazy_ide_ele = lazy_ide
        self.segfunc = segfunc
        n = len(ls)
        self.N0 = 2 ** (n - 1).bit_length()
        self.data = [self.ide_ele] * (2 * self.N0)
        self.lazy = [self.lazy_ide_ele] * (2 * self.N0)
        
        for i, x in enumerate(ls):
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
    
    def update(self, left, right, _x):
        L = self.N0 + left
        R = self.N0 + right
        x = _x
        
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] += x
                self.data[R - 1] += x
            if L & 1:
                self.lazy[L - 1] += x
                self.data[L - 1] += x
                L += 1
            L >>= 1
            R >>= 1
        for i in self.gindex(left, right):
            idx = i - 1
            self.data[idx] = self.segfunc(self.data[2 * idx + 1], self.data[2 * idx + 2]) + self.lazy[idx]

    def query(self, left, right):
        self.propagates(*self.gindex(left, right))
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
        a, b = [], []
    
        while L < R:
            if L & 1:
                a.append(L - 1)
                L += 1
            if R & 1:
                R -= 1
                b.append(R - 1)
            L >>= 1
            R >>= 1
        for i in a + b[::-1]:
            res = self.segfunc(res, self.data[i])
    
        return res


def solve():
    N = int(rl())
    S, T = [0] * N, [0] * N
    for i in range(N):
        S[i], T[i] = map(lambda x: int(x) - 1, rl().split())
    
    lazy_seg_tree = LazySegmentTree([0] * 10 ** 5, max)
    for i in range(N):
        lazy_seg_tree.update(S[i], T[i], 1)
    
    ans = 10 ** 5
    for i in range(N):
        lazy_seg_tree.update(S[i], T[i], -1)
        ans = min(ans, lazy_seg_tree.query(0, 10 ** 5 + 1))
        lazy_seg_tree.update(S[i], T[i], 1)
    print(ans)


if __name__ == '__main__':
    solve()
