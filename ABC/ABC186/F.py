import sys
from operator import add

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
    H, W, M = map(int, rl().split())
    x_to_y = [[] for _ in range(H)]
    y_to_x = [[] for _ in range(W)]
    for _ in range(M):
        xi, yi = map(lambda n: int(n) - 1, rl().split())
        x_to_y[xi].append(yi)
        y_to_x[yi].append(xi)
    
    for i in range(H):
        x_to_y[i].sort()
    for i in range(W):
        y_to_x[i].sort()
    
    ans = 0
    for i in range(W):
        if not y_to_x[i]:
            ans += H
            continue
        if y_to_x[i][0] == 0:
            break
        ans += y_to_x[i][0]
    
    init_val = [0] * W
    if x_to_y[0]:
        for i in range(x_to_y[0][0], W):
            init_val[i] = 1
    seg_tree = SegmentTree(init_val, add, 0)
    
    for i in range(1, H):
        if not x_to_y[i]:
            ans += seg_tree.query(1, W)
        elif x_to_y[i][0] == 0:
            break
        else:
            ans += seg_tree.query(1, x_to_y[i][0])
        for yj in x_to_y[i]:
            seg_tree.update(yj, 1)
    print(ans)


if __name__ == '__main__':
    solve()
