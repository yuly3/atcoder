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
        return a | b


def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


def solve():
    N = int(input())
    S = input()
    Q = int(input())
    
    init_val = [1 << ord(S[i]) - ord('a') for i in range(N)]
    seg_tree = SegmentTree(N, init_val, 0)
    
    for _ in range(Q):
        cmd, *query = input().split()
        cmd = int(cmd)
        if cmd == 1:
            i = int(query[0]) - 1
            c = query[1]
            seg_tree.update(i, 1 << ord(c) - ord('a'))
        else:
            l = int(query[0]) - 1
            r = int(query[1])
            kind = seg_tree.query(l, r)
            print(popcount(kind))


if __name__ == '__main__':
    solve()
