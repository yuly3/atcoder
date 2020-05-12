import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class BinaryIndexedTree:
    # 1-indexed
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
    
    def add(self, i, x):
        # Accessed by 0-indexed
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    def sum(self, i):
        # [0, i)
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
    N, K = map(int, rl().split())
    a = tuple(int(rl()) for _ in range(N))
    
    b = [0]
    acc = 0
    for i in range(N):
        acc += a[i]
        b.append(acc - (i + 1) * K)
    
    compress = {bi: idx for idx, bi in enumerate(sorted(b))}
    bit = BinaryIndexedTree(N + 1)
    
    ans = 0
    for bi in b:
        ans += bit.sum(compress[bi] + 1)
        bit.add(compress[bi], 1)
    print(ans)


if __name__ == '__main__':
    solve()
