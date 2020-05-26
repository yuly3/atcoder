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
    Q = int(rl())
    queries = [tuple(map(int, rl().split())) for _ in range(Q)]
    
    a = []
    for query in queries:
        if query[0] == 1:
            a.append(query[1])
    sorted_a = sorted(set(a))
    a_to_idx = {val: idx for idx, val in enumerate(sorted_a)}
    idx_to_a = {val: key for key, val in a_to_idx.items()}
    
    N = len(sorted_a)
    bit0 = BinaryIndexedTree(N)
    bit1 = BinaryIndexedTree(N)
    
    b_sm = 0
    cnt = 0
    for query in queries:
        if query[0] == 1:
            _, a, b = query
            bit0.add(a_to_idx[a], a)
            bit1.add(a_to_idx[a], 1)
            b_sm += b
            cnt += 1
        else:
            med_x = idx_to_a[bit1.bisect_left((cnt + 1) // 2) - 1]
            under_sm = bit0.sum(a_to_idx[med_x])
            under_n = bit1.sum(a_to_idx[med_x])
            over_sm = bit0.sum(N) - under_sm
            over_n = bit1.sum(N) - under_n
            print(med_x, abs(under_n * med_x - under_sm) + abs(over_n * med_x - over_sm) + b_sm)


if __name__ == '__main__':
    solve()
