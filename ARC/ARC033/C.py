import sys
readline = sys.stdin.readline


class SegmentTree:
    def __init__(self, n, init_value, ide_ele):
        self.num = 2 ** (n - 1).bit_length()
        self.ide_ele = ide_ele
        self.seg = [ide_ele] * 2 * self.num
        
        for i in range(n):
            self.seg[i + self.num - 1] = init_value[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])
    
    def update(self, _k, x):
        k = _k + self.num - 1
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])
    
    def query(self, _p, _q):
        p = _p
        q = _q
        if q <= p:
            return self.ide_ele
        
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while 1 < q - p:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res
    
    @staticmethod
    def segfunc(a, b):
        return a + b


def solve():
    Q = int(readline())
    N = 200001
    seg_tree = SegmentTree(N, [0] * N, 0)
    
    for _ in range(Q):
        t, x = map(int, readline().split())
        if t == 1:
            seg_tree.update(x, 1)
        else:
            ok, ng = N, 0
            while 1 < ok - ng:
                mid = (ok + ng) // 2
                if x <= seg_tree.query(1, mid + 1):
                    ok = mid
                else:
                    ng = mid
            seg_tree.update(ok, 0)
            print(ok)


if __name__ == '__main__':
    solve()
