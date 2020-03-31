import sys

rl = sys.stdin.readline


class SegmentTree:
    def __init__(self, n, init_value, segfunc, ide_ele):
        self.N0 = 2 ** (n - 1).bit_length()
        self.ide_ele = ide_ele
        self.data = [ide_ele] * (2 * self.N0)
        self.segfunc = segfunc
        
        for i in range(n):
            self.data[i + self.N0 - 1] = init_value[i]
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
    _, M = map(int, rl().split())
    pab = [[f(x) for f, x in zip([int, float, float], rl().split())] for _ in range(M)]
    
    p_to_idx = {p: idx for idx, p in enumerate(sorted(set(p for p, _, _ in pab)))}
    ide_ele = (1., 0.)
    N = len(p_to_idx.keys())
    init_val = [ide_ele] * N
    
    def segfunc(x, y):
        return x[0] * y[0], x[1] * y[0] + y[1]
    
    seg_tree = SegmentTree(N, init_val, segfunc, ide_ele)
    
    ans_min, ans_max = 1., 1.
    for p, a, b in pab:
        seg_tree.update(p_to_idx[p], (a, b))
        tmp = sum(seg_tree.query(0, N))
        ans_min = min(ans_min, tmp)
        ans_max = max(ans_max, tmp)
    print(ans_min)
    print(ans_max)


if __name__ == '__main__':
    solve()
