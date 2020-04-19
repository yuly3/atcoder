import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class BinaryIndexedTree:
    # 1-indexed
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
    
    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    def sum(self, i):
        res = 0
        while i:
            res += self.data[i]
            i -= i & -i
        return res
    
    def bisect_left(self, w):
        if w <= 0:
            return 0
        i = 0
        k = 1 << (self.n.bit_length() - 1)
        while 0 < k:
            if i + k <= self.n and self.data[i + k] < w:
                w -= self.data[i + k]
                i += k
            k >>= 1
        return i + 1


def solve():
    N = int(rl())
    P = list(map(int, rl().split()))
    
    p_to_idx = [0] * (N + 1)
    for i, x in enumerate(P):
        p_to_idx[x] = i + 1
    
    bit = BinaryIndexedTree(N)
    ans = 0
    for pi in range(N, 0, -1):
        idx = p_to_idx[pi]
        left = bit.sum(idx)
        bit.add(idx, 1)
        right = N - pi - left
        l0 = bit.bisect_left(left - 1) if 2 <= left else 0
        l1 = bit.bisect_left(left) if 1 <= left else 0
        r0 = bit.bisect_left(left + 2) if 1 <= right else N + 1
        r1 = bit.bisect_left(left + 3) if 2 <= right else N + 1
        cnt = 0
        if l1 != 0:
            cnt += (l1 - l0) * (r0 - idx)
        if r0 != 0:
            cnt += (r1 - r0) * (idx - l1)
        ans += pi * cnt
    print(ans)


if __name__ == '__main__':
    solve()
