import sys
from collections import Counter
from itertools import accumulate

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
    K = int(rl())
    a = []
    for _ in range(K):
        _ = rl()
        a.append(list(map(lambda n: int(n) - 1, rl().split())))
    _ = rl()
    b = list(map(lambda n: int(n) - 1, rl().split()))

    inv = [0] * K
    for i, ai in enumerate(a):
        bit = BinaryIndexedTree(21)
        cnt = 0
        for j, aij in enumerate(ai):
            cnt += j - bit.sum(aij + 1)
            bit.add(aij, 1)
        inv[i] = cnt
    
    acc_a = [[] for _ in range(K)]
    for i, ai in enumerate(a):
        ai_counter = [0] * 20
        for aij in ai:
            ai_counter[aij] += 1
        acc_a[i] = [0] + list(accumulate(ai_counter))
    
    ans = 0
    acc_x = [0] * 21
    counter_a = [Counter(ai) for ai in a]
    for bi in b[::-1]:
        ans += inv[bi]
        for key, val in counter_a[bi].items():
            ans += val * acc_x[key]
        ans %= 10 ** 9
        for j, acc_aij in enumerate(acc_a[bi]):
            acc_x[j] += acc_aij
    print(ans)


if __name__ == '__main__':
    solve()
