import sys
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class BinaryIndexedTree:
    # 1-indexed
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
    
    def add(self, _i, x):
        i = _i
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    def sum(self, _i):
        i = _i
        res = 0
        while i:
            res += self.data[i]
            i -= i & -i
        return res
    
    def bisect_left(self, _w):
        w = _w
        if w <= 0:
            return 0
        i = 0
        k = 1 << (self.n.bit_length() - 1)
        while 0 < k:
            if i + k <= self.n and self.data[i + k] < w:
                w -= self.data[i + k]
                i += k
            k = k >> 1
        return i + 1


def solve():
    MOD = 998244353
    N = int(rl())
    xy = [[0, 0] for _ in range(N)]
    for i in range(N):
        xy[i][0], xy[i][1] = map(int, rl().split())
    
    compress = sorted(xy, key=itemgetter(1))
    for i in range(N):
        compress[i][1] = i
    compress.sort(key=itemgetter(0), reverse=True)
    
    bit = BinaryIndexedTree(N)
    ups = [0] * N
    downs = [0] * N
    for i in range(N):
        com = compress[i][1] + 1
        downs[N - 1 - i] = bit.sum(com)
        ups[N - 1 - i] = i - downs[N - 1 - i]
        bit.add(com, 1)
    
    bit = BinaryIndexedTree(N)
    compress = compress[::-1]
    
    pow_of_2 = [1]
    for _ in range(N):
        pow_of_2.append(pow_of_2[-1] * 2 % MOD)
    
    ans = 0
    for i in range(N):
        com = compress[i][1] + 1
        d = bit.sum(com)
        u = i - d
        ans = (ans + (pow_of_2[d] - 1) * (pow_of_2[ups[i]] - 1) * pow_of_2[u + downs[i]]) % MOD
        ans = (ans + (pow_of_2[u] - 1) * (pow_of_2[downs[i]] - 1) * pow_of_2[d + ups[i]]) % MOD
        ans = (ans - (pow_of_2[d] - 1) * (pow_of_2[ups[i]] - 1) * (pow_of_2[downs[i]] - 1) * (pow_of_2[u] - 1)) % MOD
        ans = (ans + pow_of_2[N - 1]) % MOD
        bit.add(com, 1)
    print(ans)


if __name__ == '__main__':
    solve()
