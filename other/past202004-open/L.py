import sys

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
        ################################################################
        return res


def solve():
    N, K, D = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    if N < 1 + (K - 1) * D:
        print(-1)
        return
    
    init_val = [(ai, idx) for idx, ai in enumerate(A)]
    f = lambda a, b: a if a[0] <= b[0] else b
    seg_tree = SegmentTree(init_val, f, (10 ** 10, -1))
    
    s, t = 0, N - (K - 1) * D
    ans = []
    for _ in range(K):
        tmp, s = seg_tree.query(s, t)
        ans.append(tmp)
        s, t = s + D, t + D
    print(*ans)


if __name__ == '__main__':
    solve()
