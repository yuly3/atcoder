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
    
    def query(self, _p, _q):
        p = _p
        q = _q
        if q <= p:
            return self.ide_ele
        
        p += self.N0 - 1
        q += self.N0 - 2
        res = self.ide_ele
        while 1 < q - p:
            if p & 1 == 0:
                res = self.segfunc(res, self.data[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.data[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.data[p])
        else:
            res = self.segfunc(self.segfunc(res, self.data[p]), self.data[q])
        return res


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
    
    def segfunc(a, b):
        return a | b
    
    seg_tree = SegmentTree(N, init_val, segfunc, 0)
    
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
