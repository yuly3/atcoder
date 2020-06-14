import sys
from heapq import heappush, heappop

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
    N, Q = map(int, rl().split())
    M = 2 * 10 ** 5
    infant_to_idx = [0] * N
    infant_to_rate = [0] * N
    hq_arr = [[] for _ in range(M)]
    for i in range(N):
        a, b = map(int, rl().split())
        b -= 1
        infant_to_idx[i] = b
        infant_to_rate[i] = a
        heappush(hq_arr[b], (-a, i))
    
    ide_ele = 10 ** 10
    seg_tree = SegmentTree([ide_ele] * M, min, ide_ele)
    for i, hq in enumerate(hq_arr):
        if not hq:
            continue
        seg_tree.update(i, -hq[0][0])
    
    ans = []
    for _ in range(Q):
        c, d = map(lambda x: int(x) - 1, rl().split())
        p_idx = infant_to_idx[c]
        infant_to_idx[c] = d
        while hq_arr[p_idx]:
            if infant_to_idx[hq_arr[p_idx][0][1]] == p_idx:
                break
            heappop(hq_arr[p_idx])
        if hq_arr[p_idx]:
            seg_tree.update(p_idx, -hq_arr[p_idx][0][0])
        else:
            seg_tree.update(p_idx, ide_ele)
        
        heappush(hq_arr[d], (-infant_to_rate[c], c))
        seg_tree.update(d, -hq_arr[d][0][0])
        ans.append(seg_tree.data[0])
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
