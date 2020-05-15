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
        
        while L < R:
            if L & 1:
                res = self.segfunc(res, self.data[L - 1])
                L += 1
            if R & 1:
                R -= 1
                res = self.segfunc(res, self.data[R - 1])
            L >>= 1
            R >>= 1
        
        return res


def solve():
    N, x = map(int, rl().split())
    a = list(map(int, rl().split()))
    
    seg_tree = SegmentTree(a, min, 10 ** 15)
    ans = 10 ** 15
    for i in range(N):
        get_cost = 0
        for j in range(N):
            if i <= j:
                get_cost += seg_tree.query(j - i, j + 1)
            else:
                get_cost += min(seg_tree.query(0, j + 1), seg_tree.query(N - i + j, N))
        ans = min(ans, i * x + get_cost)
    print(ans)


if __name__ == '__main__':
    solve()
