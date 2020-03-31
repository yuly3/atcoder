def cmb(n, r, mod=10 ** 9 + 7):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    numerator, denominator = 1, 1
    for i in range(1, r + 1):
        numerator = (numerator * (n + 1 - i)) % mod
        denominator = (denominator * i) % mod
    return numerator * pow(denominator, mod - 2, mod) % mod


def cmb_replace(n, r, mod=10 ** 9 + 7):
    return cmb(n + r - 1, r, mod)


class COM:
    def __init__(self, n: int, mod: int):
        self.n = n
        self.mod = mod
        self.fact = [0] * (n + 1)
        self.factinv = [0] * (n + 1)
        self.inv = [0] * (n + 1)
        
        self.fact[0] = self.fact[1] = 1
        self.factinv[0] = self.factinv[1] = 1
        self.inv[1] = 1
        for i in range(2, n + 1):
            self.fact[i] = (self.fact[i - 1] * i) % mod
            self.inv[i] = (-self.inv[mod % i] * (mod // i)) % mod
            self.factinv[i] = (self.factinv[i - 1] * self.inv[i]) % mod
    
    def get_cmb(self, n: int, k: int):
        if (k < 0) or (n < k):
            return 0
        k = min(k, n - k)
        return self.fact[n] * self.factinv[k] % self.mod * self.factinv[n - k] % self.mod


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    
    if temp != 1:
        arr.append([temp, 1])
    if not arr:
        arr.append([n, 1])
    
    return arr


def eratosthenes(n):
    prime = [2]
    if n == 2:
        return prime
    limit = int(n ** 0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x: int):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x: int):
        return -self.parents[self.find(x)]
    
    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)
    
    def members(self, x: int):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


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
    
    def query(self, left, right):
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
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
        for i in a + (b[::-1]):
            res = self.segfunc(res, self.data[i])
        
        return res


class LazySegmentTree:
    def __init__(self, ls: list, segfunc, identity_element=0, lazy_ide=0):
        self.ide_ele = identity_element
        self.lazy_ide_ele = lazy_ide
        self.segfunc = segfunc
        n = len(ls)
        self.N0 = 2 ** (n - 1).bit_length()
        self.data = [self.ide_ele] * (2 * self.N0)
        self.lazy = [self.lazy_ide_ele] * (2 * self.N0)
        
        for i, x in enumerate(ls):
            self.data[i + self.N0 - 1] = x
        for i in range(self.N0 - 2, -1, -1):
            self.data[i] = segfunc(self.data[2 * i + 1], self.data[2 * i + 2])
    
    def gindex(self, left, right):
        L = left + self.N0
        R = right + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1
            R >>= 1
        while L:
            yield L
            L >>= 1
    
    def propagates(self, *ids):
        for i in reversed(ids):
            idx = i - 1
            v = self.lazy[idx]
            if v == self.lazy_ide_ele:
                continue
            ################################################################
            self.data[2 * idx + 1] += v >> 1
            self.data[2 * idx + 2] += v >> 1
            self.lazy[2 * idx + 1] += v >> 1
            self.lazy[2 * idx + 2] += v >> 1
            ################################################################
            self.lazy[idx] = self.lazy_ide_ele
    
    def update(self, left, right, _x):
        L = self.N0 + left
        R = self.N0 + right
        x = _x
        
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] += x
                self.data[R - 1] += x
            if L & 1:
                self.lazy[L - 1] += x
                self.data[L - 1] += x
                L += 1
            L >>= 1
            R >>= 1
            ################################################################
            x <<= 1
            ################################################################
        for i in self.gindex(left, right):
            idx = i - 1
            self.data[idx] = self.segfunc(self.data[2 * idx + 1], self.data[2 * idx + 2]) + self.lazy[idx]
    
    def query(self, left, right):
        self.propagates(*self.gindex(left, right))
        L = self.N0 + left
        R = self.N0 + right
        
        res = self.ide_ele
        while L < R:
            if R & 1:
                R -= 1
                res = self.segfunc(res, self.data[R - 1])
            if L & 1:
                res = self.segfunc(res, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return res
